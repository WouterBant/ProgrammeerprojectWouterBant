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
    path("addLike/<int:id>", views.addLike, name="addLike"),
    path("delete_video/<int:id>", views.delete_video, name="delete_video"),
    path("update_information/<int:id>", views.update_information, name="update_information"),
    path("search", views.search, name="search"),
    path("display_category", views.display_category, name="display_category"),
    path("go_to_profile/<int:id>", views.go_to_profile, name="go_to_profile"),
    path("removeSaved/<str:title>", views.removeSaved, name="removeSaved"),
    path("addSaved/<str:title>", views.addSaved, name="addSaved"),
    path("removeLike/<str:title>", views.removeLike, name="removeLike"),
    path("addLike/<str:title>", views.addLike, name="addLike"),
    path("delete_from_saved/<str:title>", views.delete_from_saved, name="delete_from_saved"),
    path("removeSub/<str:title>", views.removeSub, name="removeSub"),
    path("addSub/<str:title>", views.addSub, name="addSub"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
