# Generated by Django 4.1.3 on 2022-11-22 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_puppy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Videos_Posted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('premium', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('video_file', models.FileField(upload_to='')),
                ('active', models.BooleanField(default=True)),
                ('time_posted', models.TimeField(auto_now=True)),
                ('category_video', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category_video', to='videos.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(default=0, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('video_saved', models.ManyToManyField(related_name='video_saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
