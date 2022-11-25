from django.contrib import admin
from .models import Category, Videos_Posted, Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Videos_Posted)
admin.site.register(Profile)