
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class login(models.Model):
    Name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    number = models.CharField(max_length=20,null=True)
    passw = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.Name

class register(models.Model):
    Name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    number = models.CharField(max_length=20,null=True)
    passw = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.Name
