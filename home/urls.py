from django.urls import path
from .views import (home_view, tweet_like)

urlpatterns = [
    path('', home_view, name='home'),
    path('liked/<int:tweet_id>', tweet_like, name='liked'),
]
