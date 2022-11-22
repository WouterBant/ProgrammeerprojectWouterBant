from django.contrib import admin
from .models import Puppy, Category, Videos_Posted

# Register your models here.
admin.site.register(Puppy)
admin.site.register(Category)
admin.site.register(Videos_Posted)