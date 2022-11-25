from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Videos_Posted, Category, Comments, Profile


def index(request):
    data = Videos_Posted.objects.all()
    return render(request, "videos/index.html", {
        "data": data,
        "cats": Category.objects.all()
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
    data = Videos_Posted.objects.order_by('likes').reverse()
    return render(request, "videos/leaderboard.html", {
        "data": data
    })

def subscriptions(request):
    return render(request, "videos/subscriptions.html")

def upload(request):
    return render(request, "videos/upload.html", {
        "cats": Category.objects.all()
    })

def profile(request):
    user = request.user
    data = Profile.objects.get(person=user)
    vids = Videos_Posted.objects.filter(creator=user)
    return render(request, "videos/profile.html", {
        "data": data,
        "vids": vids
    })

def saved(request):
    return render(request, "videos/saved.html")

def video(request, title):
    if request.method == "GET":
        try:
            data = Videos_Posted.objects.get(title=title)
        except:
            data = None
        allComments = Comments.objects.filter(comment_video=data)
        # isOwner = request.user.username == data.owner.username
        return render(request, "videos/video.html", {
            'data': data,
            'allComments': allComments,
            # 'isOwner': isOwner
        })
    

def upload_video(request):
    creator = request.user
    title = request.POST['title']
    description = request.POST['description']
    category = Category.objects.get(category=request.POST['category'])
    new_video = Videos_Posted(
        title = title,
        description = description,
        video_file = request.FILES['video'],
        thumbnail = request.FILES['thumbnail'],
        category_video = category,
        creator = creator
    )
    new_video.save()
    return HttpResponseRedirect(reverse(index))

def addComment(request, id):
    userNow  = request.user
    data = Videos_Posted.objects.get(pk=id)
    title = data.title
    message = request.POST['newComment']

    newComment = Comments(
        author=userNow,
        comment_video=data,
        message=message
    )
    newComment.save()
    return HttpResponseRedirect(reverse("video", args=(title, )))

def addLike(request, id):
    userNow  = request.user
    data = Videos_Posted.objects.get(pk=id)
    data.likes += 1
    title = data.title
    data.save(update_fields=["likes"]) 

    return HttpResponseRedirect(reverse("video", args=(title,)))

def delete_video(request, id):
    Videos_Posted.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse(index))

def update_information(request, id):
    data = Profile.objects.get(pk=id)
    data.profile_name = request.POST['new_username']
    data.profile_description = request.POST['new_description']
    data.save()
    return HttpResponseRedirect(reverse(index))

def search(request):
    search_term = request.POST['term']
    data = Videos_Posted.objects.all()
    res = []
    for obj in data:
        if search_term in obj.title:
            res.append(obj)
    return render(request, "videos/search.html", {
        "data": res
    })

def display_category(request):
    cat = request.POST['category']
    cats = Category.objects.get(category=cat)
    list_of_videos = Videos_Posted.objects.filter(category_video=cats)
    return render(request, "videos/index.html", {
        "data": list_of_videos,
        "cats": Category.objects.all()
    })

def save_video(request, id):
    pass

def go_to_profile(request, id):
    record = Videos_Posted.objects.filter(id=id)
    print(record)
    # print("\n\n\n\n\n\n\n")
    # Profile.objects.get(person=user)
    return render(request, "videos/go_to_profile.html", {
        "data": record
    })
