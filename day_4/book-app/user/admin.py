from django.contrib import admin

# models
from .models import User, Profile

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)