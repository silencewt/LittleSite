# settings.py  AUTH_USER_MODEL = "profiles.UserProfile"
from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
	des = models.CharField(max_length=100, null=True)
	
