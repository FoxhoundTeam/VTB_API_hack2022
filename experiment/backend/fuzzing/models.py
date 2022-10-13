from django.db import models

# Create your models here.

class Task(models.Model):
    status=models.IntegerField()
    # name = 
    # result=