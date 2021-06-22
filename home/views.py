from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Local
from tweets.models import (Tweet, Comment)


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    tweets = Tweet.objects.order_by('-twt_time')

    # TweetLike.objects.filter(tweet=tweets).count()
    # get total likes on post
    context = {'tweets': tweets}
    return render(request, 'home/home.html', context)


# Liking and unliking the post
def tweet_like(request, tweet_id):
    twt = Tweet.objects.get(id=tweet_id)
    if request.user in twt.likes.all():
        print('un like')
        twt.likes.remove(request.user)
    else:
        print('like')
        twt.likes.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def tweet_detail(request, tweet_id):
    twt = Tweet.objects.get(id=tweet_id)
    comments = Comment.objects.filter(tweet=twt)
    context = {'tweet': twt, 'comments': comments, 'likes': twt.likes}
    return render(request, 'home/tweet_detail.html', context)
