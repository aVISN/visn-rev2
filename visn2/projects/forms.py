# docs forms: https://docs.djangoproject.com/en/3.2/topics/forms/ 

from pyexpat import model
from statistics import mode
from xml.dom import ValidationErr
# from attr import attrs
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import ProjFile, Project, Project
from accounts.models import DjUser


class ProjFileForm(forms.ModelForm):
    class Meta:
        model = ProjFile
        exclude = ['author', ]

class NewProjForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []
    freelancer = forms.ModelChoiceField(queryset=DjUser.objects.filter(userType=2))
    client = forms.ModelChoiceField(queryset=DjUser.objects.filter(userType=1))