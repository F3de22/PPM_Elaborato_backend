from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import login
from . import models


# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = models.UserCreateForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('homepage')
    else:
        form = models.UserCreateForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    try:
        auth.logout(request)
        messages.info(request,"User Logged Out!")
        return redirect('/')
    except:
        return redirect("/")


def logout(request):
    try:
        auth.logout(request)
        messages.info(request,"User Logged Out!")
        return redirect('/')
    except:
        return redirect("/")
