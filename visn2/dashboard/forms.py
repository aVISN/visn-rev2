# docs forms: https://docs.djangoproject.com/en/3.2/topics/forms/ 

from pyexpat import model
from statistics import mode
from xml.dom import ValidationErr
from attr import attrs
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import ProjFile, Project, Upload, DjUser, Project

# ModelForm: https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class UploadForm(forms.ModelForm):
    class Meta: 
        model = Upload
        fields = ('description', 'comments', 'filename')

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
        

# class MyUserForm(forms.Form):
#     name = forms.CharField(min_length=5, label='name', required=True)
#     password = forms.CharField(min_length=4, label='password', required=True)
#     password2 = forms.CharField(min_length=4, label='confirm password', required=True)
#     userType = forms.ChoiceField(choices=[(1,'client'), (2, 'programer')], label='user type')

#     def clean(self):
#         ps = self.cleaned_data.get('password')
#         ps2 = self.cleaned_data.get('password2')
#         if ps == ps2:
#             return self.cleaned_data
#         self.add_error('password2', ValidationErr('confirm password error!'))

# class LoginForm(forms.Form):
#     name = forms.CharField(min_length=5, label='name', required=True)
#     password = forms.CharField(min_length=4, label='password', required=True)

class MyUserCreationForm(UserCreationForm):
    userType = forms.ChoiceField(choices=[(1,'client'), (2, 'Freelancer')], label='user type', required=True)
    
    class Meta(UserCreationForm.Meta):
        model = DjUser
        fields = ['username', 'password1', 'password2', 'userType']

class MessageForm(forms.Form):
    mto = forms.CharField(min_length=5, label='to name', required=True, widget=forms.HiddenInput())
    message = forms.CharField(widget=widgets.Textarea(attrs={'rows': 1}), label='message text', required=True)
