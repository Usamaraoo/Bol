from django.urls import path
from .views import (home_view, tweet_like, tweet_detail)

urlpatterns = [
    path('', home_view, name='home'),
    path('liked/<int:tweet_id>', tweet_like, name='liked'),
    path('tweet_detail/<int:tweet_id>', tweet_detail, name='tweet_detail')
]
