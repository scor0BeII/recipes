from django.urls import path, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RegisterForm


@login_required(login_url=reverse_lazy("login"))
def profile(request):
    return render(request, "profile.html")
def login_view(request):
    redirect_url = reverse("profile")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, "login.html")
    else: 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        return render(request, "login.html", context={"error" : "Пользователь не найден"})
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("profile"))
    else:
        form = RegisterForm()
    return render(request, "regist.html", {'form':form})
