from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
# Local
from tweets.models import Tweet


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    tweets = Tweet.objects.order_by('-twt_time')
    context = {'tweets': tweets}
    return render(request, 'home/home.html', context)
