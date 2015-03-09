from django.db import models
from account.models import User
from django import forms

# Create your models here.
class Share(models.Model):
	TYPE_CHOICES = (
			('img', 'image'),
			('url', 'url'),
			('text', 'text'),
			('file', 'file'),
			('music', 'music'),
			('user', 'user'),
			('share','share')
		)
	name = models.CharField(max_length=40, null=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	type = models.CharField(max_length=10,choices=TYPE_CHOICES)
	content = models.TextField()

