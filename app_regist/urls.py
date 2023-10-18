from django.shortcuts import render
from django.urls import path
from .views import login_view, profile, logout_view, register

urlpatterns = [
    path("login/", login_view, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_view, name="logout"),
    path("regist/", register, name="register")
    
]