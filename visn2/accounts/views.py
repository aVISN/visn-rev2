from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .models import *
from .forms import CreateUserForm, MyUserCreationForm

def registerPage(request):
    form = MyUserCreationForm()#CreateUserForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)#CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('frontpage')


# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     fields = '__all__'
    # redirect_authenticated_user = True

    # def get_success_url(self):
    #     return reverse_lazy('successLogin')


def postLoginView(request):
    return HttpResponse('view after success Login')
