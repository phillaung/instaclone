from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm
from django.views.generic.edit import CreateView

# Create your views here.
@login_required
def home(request):
    tweets = Tweet.objects.filter(user=request.user)
    return render(request, 'home.html', { 'tweets': tweets })

@login_required
def detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'detail.html', { 'tweet': tweet })

@login_required
def create(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        new_tweet = form.save(commit=False)
        new_tweet.user = request.user
        new_tweet.save()
        return redirect('/')

def about(request):
    return render(request, 'about.html')
