from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Local
from tweets.models import Tweet
from tweets.models import TweetLike


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
    # the tweet will be liked and TweetLike instance will be create
    # if the tweet is already liked will remove the TweetLike instance and remove like from tweet
    try:
        TweetLike.objects.create(user=request.user, liked=True, tweet=twt)
        twt.likes += 1
    except:
        TweetLike.objects.get(user=request.user, tweet=twt).delete()
        twt.likes -= 1
        print('Likes Now', twt.likes)
    twt.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
