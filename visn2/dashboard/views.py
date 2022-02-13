from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy



def dashboardView(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)
