from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet
# Create your views here.
@login_required
def home(request):
    tweets = Tweet.objects.filter(user=request.user)
    return render(request, 'home.html', { 'tweets': tweets })

@login_required
def detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'detail.html', { 'tweet': tweet })

def about(request):
    return render(request, 'about.html')