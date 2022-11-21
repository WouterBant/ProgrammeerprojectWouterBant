from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# class Category(models.Model):
#     category = models.CharField(max_length=50)

#     def __str__(self):
#         return self.category

# class Videos_Posted(models.Model):
#     title = models.CharField(max_length=40)
#     description = models.CharField(max_length=500)
#     premium = models.BooleanField(default=False)
#     thumbnail = models.CharField(max_length=300) # wat moet dit worden?
#     video_file = models.CharField(max_length=300) # wat moet dit worden?
#     category_video = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_video")
#     active = models.BooleanField(default=True)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
#     video_saved = models.ManyToManyField(User, related_name="video_saved")
#     time_posted = models.TimeField(auto_now=True)
#     likes = models.ManyToManyField(User, related_name="likes") # is dit goed?

#     def __str__(self):
#         return self.title

# class Comments(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
#     comment_video = models.ForeignKey(Videos_Posted, on_delete=models.CASCADE, related_name="comment_video")
#     message = models.CharField(max_length=500)

#     def __str__(self):
#         return f"{self.author} comment on {self.listing}"