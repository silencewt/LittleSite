from django.db import models
from django import forms

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	nickname = models.CharField(max_length=20, null = True)
	des = models.TextField(null = True)
	birthday = models.DateField(null = True)
	level = models.IntegerField(null = True)

class UserRegisterForm(forms.Form):
	username=forms.CharField(label=(u'username'),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))      
 	password=forms.CharField(label=(u'password'),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))  
	email=forms.EmailField(label=(u'email'),max_length=30,widget=forms.TextInput(attrs={'size': 30,}))

class UserLoginForm(forms.Form):
	username=forms.CharField(label=(u'username'),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))      
 	password=forms.CharField(label=(u'password'),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))  
