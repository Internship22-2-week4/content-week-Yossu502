from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
  """
  Custom user model
  """
  email = models.EmailField(
    'email address',
    unique=True,
    error_messages={
      'unique': 'A user with that email already exists.'
    }
  )

  phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone Number is invalid'
  )

  phone_number = models.CharField(
    validators=[phone_regex],
    max_length=20,
    blank=True,
    null=True
  )

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  is_client = models.BooleanField(
    'client status',
    default=False,
    help_text='Designates whether the user can log into the admin sites'
  )

  is_verified = models.BooleanField(
    'verified status',
    default=True,
    help_text='Designates whether the user has verified ther email address'
  )

  def __str__(self) -> str:
    return self.username

  def get_short_name(self) -> str:
    return super().get_short_name()


class Profile(models.Model):
  """
  Profile Model
  """

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone Number is invalid'
  )
  
  phone_number = models.CharField(
    validators=[phone_regex],
    max_length=20,
    blank=True,
    null=True
  )

  country = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self) -> str:
    return self.user.username