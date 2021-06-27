from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime
# Local
from accounts.models import (UserNotification, UserProfile)
from tweets.models import (Tweet, Comment)


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    searched_users = None
    if request.method == 'GET':
        get_name = request.GET.get('username')
        if get_name is not None:
            searched_users = UserProfile.objects.filter(username__icontains=get_name)
    tweets = Tweet.objects.order_by('-twt_time')
    total_notifications = UserNotification.objects.filter(user=request.user)
    print('notify',total_notifications)
    context = {'tweets': tweets, 'total_notifications': total_notifications, 'searched_users': searched_users}
    return render(request, 'home/home.html', context)


# Liking and unliking the post
def tweet_like(request, tweet_id):
    twt = Tweet.objects.get(id=tweet_id)
    if request.user in twt.likes.all():
        twt.likes.remove(request.user)

    else:
        twt.likes.add(request.user)
        # Generating notification
        UserNotification.objects.create(user=twt.user, notification_time=datetime.now(),tweet=twt,
                                        from_user=request.user, notification=f'{request.user} liked your tweet'
                                        )
        print('tweet liked')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def tweet_detail(request, tweet_id):
    twt = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(user=request.user, comment=comment, tweet=twt, comment_time=datetime.now())
        twt.comments += 1
        twt.save()
        # generation notification for the user
        UserNotification.objects.create(user=twt.user, notification_time=datetime.now(),tweet=twt,
                                        from_user=request.user, notification=f'{request.user} commented on your tweet')

    comments = Comment.objects.filter(tweet=twt)
    context = {'tweet': twt, 'comments': comments, 'likes': twt.likes}
    return render(request, 'home/tweet_detail.html', context)
