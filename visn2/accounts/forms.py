from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# ----- added from Mingyuan's forms
from pyexpat import model
from statistics import mode
from xml.dom import ValidationErr
# from attr import attrs
# from django import forms
from django.forms import widgets
# from django.contrib.auth.forms import UserCreationForm
# from .models import ProjFile, Project, Upload, DjUser, Project
from .models import DjUser
# ----------------------

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



# ----- added from Mingyuan's forms
class MyUserCreationForm(UserCreationForm):
    userType = forms.ChoiceField(choices=[(1,'client'), (2, 'Freelancer')], label='user type', required=False)#True)
    
    class Meta(UserCreationForm.Meta):
        model = DjUser
        fields = ['username', 'password1', 'password2', 'userType']


# --------