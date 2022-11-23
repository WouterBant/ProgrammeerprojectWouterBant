from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
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
    path("video/<str:title>", views.video, name="video"),
    path("saved", views.saved, name="saved"),
    path("upload_video", views.upload_video, name="upload_video"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)