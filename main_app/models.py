from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    content = models.CharField()
    image_url = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tweet_id': self.id})
    
    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    content = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
            return reverse('detail', kwargs={'tweet_id': self.id})
   
    class Meta:
        ordering = ['-created_at']