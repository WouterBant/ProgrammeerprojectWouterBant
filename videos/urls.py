from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("subscriptions", views.subscriptions, name="subscriptions"),
    path("upload", views.upload, name="upload"),
    path("profile", views.profile, name="profile"),
    path("saved", views.saved, name="saved")
]

urlpatterns += staticfiles_urlpatterns()