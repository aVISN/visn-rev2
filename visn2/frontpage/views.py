from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

# from django.contrib.auth.views import LoginView

def tempFrontPageView(request):
    return HttpResponse('temp view for front page')
