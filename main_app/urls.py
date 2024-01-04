from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tweets/<int:tweet_id>/', views.detail, name='detail'),
    path('tweets/tweets_create/', views.tweets_create, name='tweet_create'),
    path('tweets/<int:pk>/update', views.TweetUpdate.as_view(), name='tweet_update'),
    path('tweets/<int:pk>/delete', views.TweetDelete.as_view(), name='tweet_delete'),
    path('tweets/<int:tweet_id>/comments_create/', views.comments_create, name='comment_create'),
]