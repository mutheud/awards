from django.contrib import admin
from awards.views import *
from .models import Rate, Profile, Project
# Register your models here.

admin.site.register(Rate)
admin.site.register(Profile)
admin.site.register(Project)
