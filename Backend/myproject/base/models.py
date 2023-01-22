from django.db import models
from datetime import datetime,date
# Create your models here.

class CreateLogin(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=20,primary_key=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + " " + self.lastname
