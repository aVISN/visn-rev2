# after modifying models.py must migrate changes to database:
# ./manage.py makemigrations
# ./manage.py migrate

from django.db import models
from datetime import datetime
from django.conf import settings


# Create your models here.
class Project(models.Model):
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='freelancer')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=100, null=False)
    # deadline = models.DateTimeField()
    deadline = models.DateField()
    discription = models.TextField()

    def __str__(self):
        return self.name

class ProjFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    filename = models.FileField(upload_to='')
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class UserProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)