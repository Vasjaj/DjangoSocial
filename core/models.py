from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneF    bio = models.TextField(max_length=500, blank=True)ield(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=True)
    surname = models.TextField(max_length=100, blank=True)
