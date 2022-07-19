from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.URLField(max_length=200, blank=True)
  biography = models.TextField(blank=True, max_length=200)
  phone_number = models.CharField(max_length=20, blank=True)
  picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
  created = models.DateField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.user.username
