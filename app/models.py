from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)
    LL=models.IntegerField()
    UL=models.IntegerField()
    timetaken=models.CharField(max_length=100)
    algorithm=models.CharField(max_length=100)
    no_of_primes=models.IntegerField()
