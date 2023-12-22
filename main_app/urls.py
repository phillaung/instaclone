from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tweets/<int:tweet_id>/', views.detail, name='detail')
]