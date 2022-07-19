from django.db import models

# Create your models here.

class User(models.Model):
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=25)
  is_admin = models.BooleanField(default=False)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  bio = models.TextField(blank=True)
  birthday = models.DateField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  country = models.CharField(max_length=100, default=False)
