from .views import *
from django.urls import path

urlpatterns = [
    path('', mainPage.as_view(), name='home'),
    path('about', AboutPage, name='about'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logoutUser, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>', ShowPost, name='post'),
    path('search/', Search.as_view(), name='search'),
]