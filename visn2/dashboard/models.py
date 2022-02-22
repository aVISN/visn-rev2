from django.db import models

# Create your models here.
# after modifying models.py must migrate changes to database:
# ./manage.py makemigrations
# ./manage.py migrate
from datetime import datetime
from email.policy import default
from operator import mod
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# models: https://docs.djangoproject.com/en/3.2/topics/db/models/
class Upload(models.Model):
    description = models.CharField(max_length=100)
    comments = models.TextField(blank=True)
    filename = models.FileField(upload_to='')

    def __str__(self):
        return self.description

# class MyUser(models.Model):
#     name = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=512)
#     userType = models.IntegerField(default=1) #1 client 2: programer


# class Messages(models.Model):
#     mfrom = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mfrom')
#     msg = models.TextField()
#     mto = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mto')


class DjUser(AbstractUser):
    userType = models.IntegerField(choices=((1, 'client'), (2, 'Freelancer')))

class Message(models.Model):
    mfrom = models.ForeignKey('DjUser', on_delete=models.CASCADE, related_name='mfrom')
    msg = models.TextField()
    mto = models.ForeignKey('DjUser', on_delete=models.CASCADE, related_name='mto')
    msgTime = models.DateTimeField(default=datetime.now)

class Project(models.Model):
    freelancer = models.ForeignKey('DjUser', on_delete=models.CASCADE, related_name='freelancer')
    client = models.ForeignKey('DjUser', on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=100, null=False)
    deadline = models.DateTimeField()
    discription = models.TextField()

    def __str__(self):
        return self.name

class ProjFile(models.Model):
    project = models.ForeignKey('project', on_delete=models.CASCADE, related_name='project')
    filename = models.FileField(upload_to='')
    comment = models.TextField()
    author = models.ForeignKey('DjUser', on_delete=models.CASCADE, related_name='author')