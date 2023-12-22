from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    content = models.CharField()
    image_url = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)