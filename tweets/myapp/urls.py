from django.urls import path
from myapp import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweets/', views.tweet_list, name='tweet_list'),  # This is /tweets/
    path('tweets/mytweets/', views.tweet_list, name='my_tweets'),  # This is /tweets/mytweets/
    path('tweet/', RedirectView.as_view(pattern_name='my_tweets', permanent=False), name='tweet_alias'),
    path('tweets/new/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
