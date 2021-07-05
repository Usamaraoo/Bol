import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
# local
from tweets.models import Tweet
from .models import UserProfile, UserNotification
from .forms import SignUpForm, LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(username=credentials['username'], password=credentials['password'])
            print()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'accounts/log_in.html', context)


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/sign_up.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print('username',username,'password',raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('/')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def profile_view(request, username):
    profile_user = UserProfile.objects.get(username=username)
    profile_user_tweet = Tweet.objects.filter(user=profile_user)

    context = {'profile_user': profile_user, 'tweets': profile_user_tweet}
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def following_view(request, username):
    profile_user = UserProfile.objects.get(username=username)
    print(profile_user)
    following = profile_user.following.all()
    followers = profile_user.followers.all()
    context = {'following': following, 'followers': followers}
    return render(request, 'accounts/followers.html', context)


# if the user following the user then unfollow or follow vice versa
def follow_unfollow(request, username):
    user = UserProfile.objects.get(username=username)
    if user in request.user.following.all():
        # removing the current user from profile follower list and current user following list
        request.user.following.remove(user)
        user.followers.remove(request.user)
        print('unfollowed')
    else:
        # adding the current user to profile follower list and current user following list
        user.followers.add(request.user)
        request.user.following.add(user)
        UserNotification.objects.create(notification_time=datetime.datetime.now(), from_user=request.user,
                                        user=user, notification=f'{request.user} started following you')
        print('followed')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def notifications_view(request):
    notifications = UserNotification.objects.filter(user=request.user)
    # notifications.update(active=True)
    context = {'notifications': notifications}
    return render(request, 'accounts/user_notifications.html', context)
