from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Local
from accounts.models import UserProfile
from .models import Messages, MessageNotification


@login_required(login_url='login')
def chat_list(request, user_name):
    user = UserProfile.objects.get(username=user_name)
    message_list = MessageNotification.objects.filter(for_user=user).order_by('-notification_time')
    context = {'message_list': message_list}
    return render(request, 'chat/message_list.html', context)


@login_required(login_url='login')
def chat_room(request, chat_for_user):
    chat_user = UserProfile.objects.get(username=chat_for_user)
    my_msg = Messages.objects.filter(to_user=request.user   , from_user=chat_user)
    other_user_msgs = Messages.objects.filter(to_user=chat_user, from_user=request.user)
    print(f'other user {chat_user} message',other_user_msgs)

    notification = MessageNotification.objects.get(for_user=request.user, notification=chat_user)
    notification.active = False
    notification.save()
    context = {'other_user_msgs': other_user_msgs, 'chat_user': chat_user,
               'whole_chat': zip(other_user_msgs, list(my_msg))}
    return render(request, 'chat/room.html', context)
