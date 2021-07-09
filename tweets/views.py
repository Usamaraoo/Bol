from django.shortcuts import render
from django.shortcuts import HttpResponse
# Local


# Create your views here.

def tweet_view(request):
    return HttpResponse('<h1> Tweets </h1>')
