from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_to_chat>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/', consumers.ChatConsumer.as_asgi()),
]