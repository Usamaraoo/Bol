from django.urls import path
from .views import (login_view, signup_view, profile_view, following_view, follow_unfollow, notifications_view)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('following/<str:username>', following_view, name='following_view'),
    path('follow_or_unfollow/<str:username>', follow_unfollow, name='follow_unfollow'),
    path('notify/', notifications_view, name='notify'),

]
