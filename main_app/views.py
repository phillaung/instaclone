from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet
# Create your views here.
@login_required
def home(request):
    tweets = Tweet.objects.filter(user=request.user)
    return render(request, 'home.html', { 'tweets': tweets })

def about(request):
    return render(request, 'about.html')