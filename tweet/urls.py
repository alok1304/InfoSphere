from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list,name='tweet_list'),
    path('create/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete,name='tweet_delete'),
    path('register/', views.register,name='register'),
    path('search/', views.search_tweets,name='search_tweets'),
    path('news/', views.news_view,name='news_view'),
    path('jokes/', views.joke_view,name='joke_view'),
    path('upvote/<int:tweet_id>/', views.upvote_tweet, name='upvote_tweet'),
    path('downvote/<int:tweet_id>/', views.downvote_tweet, name='downvote_tweet'),
]
