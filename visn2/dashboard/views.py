from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy



def tempView(request):
    return HttpResponse('temp view for dashboard')
