from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class customer(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Deposit(models.Model):
    amount=models.FloatField()
    description=models.CharField(max_length=50)
    


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # balance = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
    balance = models.FloatField(default=0)

    def __str__(self):
        return f"Balance for {self.user.username}"
