from django.shortcuts import render, redirect
from .models import Tweet, Comment
from .forms import TweetForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    tweets = Tweet.objects.filter(user=request.user)
    return render(request, 'home.html', { 'tweets': tweets })

@login_required
def detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    comments = Comment.objects.filter(tweet=tweet_id)
    return render(request, 'detail.html', { 
       'tweet': tweet,
       'comments': comments,
    })

@login_required
def tweets_create(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        new_tweet = form.save(commit=False)
        new_tweet.user = request.user
        new_tweet.save()
        return redirect('/')
    
@login_required
def comments_create(request, tweet_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.tweet = Tweet.objects.get(id=tweet_id)
        new_comment.save()
        return redirect('detail', tweet_id=tweet_id)
    
class TweetUpdate(LoginRequiredMixin, UpdateView):
  model = Tweet
  fields = ['content']

class TweetDelete(LoginRequiredMixin, DeleteView):
  model = Tweet
  success_url = '/'

def about(request):
    return render(request, 'about.html')
