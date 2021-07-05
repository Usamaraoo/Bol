import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from datetime import datetime
# Local
from accounts.models import UserProfile
from chat.models import Messages, MessageNotification


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_to_chat = self.scope['url_route']['kwargs']['user_to_chat']
        self.room_name = 'chat'
        self.room_group_name = 'chat_group'
        print(self.scope['url_route'])
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('tis is message', message)
        self.sender = text_data_json['sender']
        # Send message to room group
        await self.create_message(message=message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.sender
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))

    @database_sync_to_async
    def create_message(self, message):
        other_user = UserProfile.objects.get(username=self.user_to_chat)
        print('the other user', other_user)
        if message is not None:
            Messages.objects.create(from_user=self.scope['user'], to_user=other_user, message=message,
                                    message_time=datetime.now())
        # Getting the chat notification for the user otherwise creating it
        notify, created = MessageNotification.objects.get_or_create(for_user=other_user,
                                                                    notification=self.scope['user'])
        # On new message marking it as unread
        if created is not True:
            notify.active = True
            notify.notification_time = datetime.now()
            notify.save()
