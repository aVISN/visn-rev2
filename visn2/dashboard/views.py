from django.shortcuts import render
from django.http import HttpResponse

def tempView(request):
    return HttpResponse('this is a temp view')
