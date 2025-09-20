from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(default=None,max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)


class product(models.Model):
    name = models.CharField(default=None,max_length=100)
    price = models.IntegerField(default=20000)
    category = models.TextField(default="high")
    