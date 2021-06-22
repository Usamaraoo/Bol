from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# local
from tweets.models import Tweet
from .models import UserProfile


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'accounts/log_in.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile_view(request, username):
    profile_user = UserProfile.objects.get(username=username)
    profile_user_tweet = Tweet.objects.filter(user=profile_user)

    context = {'profile_user': profile_user, 'tweets': profile_user_tweet}
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def following_view(request, username):
    profile_user = UserProfile.objects.get(username=username)
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
        user.followers.remove(user)
    else:
        # adding the current user to profile follower list and current user following list
        user.followers.add(user)
        request.user.following.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
