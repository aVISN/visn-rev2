from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'dashboard/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('temp')

def tempView(request):
    return HttpResponse('this is a temp view')
