from django.db import models
from  .models import *

# Create your models here.


class recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="image")


class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True)
    is_check = models.BooleanField(null=True,blank=True)