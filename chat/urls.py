from django.urls import path

from . import views

urlpatterns = [
    # path('', views.chat_view, name='chat_view'),
    path('<str:chat_for_user>', views.chat_room, name='chat_room'),
    path('chat/list/<str:user_name>', views.chat_list, name='chat_list'),
]
