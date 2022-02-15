from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from datetime import datetime

# Local
from accounts.models import (UserNotification, UserProfile)
from tweets.models import (Tweet, Comment)
from tweets.forms import TweetForm


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    searched_users = None

    if request.method == 'GET':
        get_name = request.GET.get('username')
        if get_name is not None:
            searched_users = UserProfile.objects.filter(
                username__icontains=get_name)
    tweets = Tweet.objects.order_by('-twt_time')
    total_notifications = UserNotification.objects.filter(
        user=request.user, active=True)
    # Setting the cookie for the notifications count show
    request.session['notification_count'] = UserNotification.objects.filter(
        user=request.user, active=True).count()
    print(request.session['notification_count'], 'these are cookie')
    twt_form = TweetForm(request.POST or None)
    data = {}
    if request.is_ajax:
        if twt_form.is_valid():
            print('done')
            tweet = twt_form.save(commit=False)

            # tweet.tweet = twt_form.cleaned_data.get('tweet')
            tweet.user = request.user
            tweet.twt_time = datetime.now()
            tweet.save()
            data['tweet'] = twt_form.cleaned_data.get('tweet')
            data['tweet_id'] = tweet.id
            data['status'] = 'ok'

            return JsonResponse(data)

    context = {'tweets': tweets, 'total_notifications': total_notifications, 'searched_users': searched_users,
               'form': twt_form}
    return render(request, 'home/home.html', context)


# Liking and unliking the post
def tweet_like(request, tweet_id):
    twt = Tweet.objects.get(id=tweet_id)
    if request.user in twt.likes.all():
        twt.likes.remove(request.user)

    else:
        twt.likes.add(request.user)
        # Generating notification
        UserNotification.objects.create(user=twt.user, notification_time=datetime.now(), tweet=twt,
                                        from_user=request.user, notification=f'{request.user} liked your tweet'
                                        )
        print('tweet liked')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def tweet_detail(request, tweet_id):
    twt = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(
            user=request.user, comment=comment, tweet=twt, comment_time=datetime.now())
        twt.comments += 1
        twt.save()
        # generation notification for the user
        UserNotification.objects.create(user=twt.user, notification_time=datetime.now(), tweet=twt,
                                        from_user=request.user, notification=f'{request.user} commented on your tweet')

    comments = Comment.objects.filter(tweet=twt)
    # deactivating all the notification to related post ( When the User open the tweet to related posts)
    notification = UserNotification.objects.filter(
        tweet=twt, user=request.user).update(active=False)

    print('Current Post notificaiton', notification)
    context = {'tweet': twt, 'comments': comments, 'likes': twt.likes}
    return render(request, 'home/tweet_detail.html', context)
