from django.db import models

# Create your models here.


class Customers(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200, unique=True)
    phone = models.IntegerField( unique=True)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    
