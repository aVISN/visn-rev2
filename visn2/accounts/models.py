from django.db import models

# ----- added from Mingyuan's Models
from datetime import datetime
from email.policy import default
from operator import mod
from pyexpat import model
from random import choices
# from django.db import models
from django.contrib.auth.models import AbstractUser



class DjUser(AbstractUser):
    userType = models.IntegerField(default=1,choices=((1, 'client'), (2, 'Freelancer')))

#-------