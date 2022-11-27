# Generated by Django 4.1.3 on 2022-11-25 10:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='videos', to='videos.videos_posted'),
        ),
        migrations.AddField(
            model_name='videos_posted',
            name='video_saved',
            field=models.ManyToManyField(blank=True, related_name='video_saved', to=settings.AUTH_USER_MODEL),
        ),
    ]
