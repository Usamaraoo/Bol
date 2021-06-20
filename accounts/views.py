from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
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
    cur_user = request.user
    profile_user = UserProfile.objects.get(username=username)
    print('my profile')
    profile_user_tweet = Tweet.objects.filter(user=profile_user)

    context = {'profile_user': profile_user, 'tweets': profile_user_tweet}
    return render(request, 'accounts/profile.html', context)
