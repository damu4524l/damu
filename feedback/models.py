from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    name=models.CharField(max_length=30)
    idnum=models.CharField(max_length=30)
    email=models.EmailField()
    collage=models.CharField(max_length=100)
    summary=models.CharField(max_length=2000)
    date=models.DateTimeField()


    def __str__(self):
        return self.name