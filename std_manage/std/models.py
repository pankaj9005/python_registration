from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)