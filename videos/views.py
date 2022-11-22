from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Puppy, Videos_Posted


def index(request):
    return render(request, "videos/index.html", {
        "dog": Videos_Posted.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "videos/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "videos/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "videos/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "videos/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "videos/register.html")

def leaderboard(request):
    return render(request, "videos/leaderboard.html")

def subscriptions(request):
    return render(request, "videos/subscriptions.html")

def upload(request):
    return render(request, "videos/upload.html")

def profile(request):
    return render(request, "videos/profile.html")

def saved(request):
    return render(request, "videos/saved.html")