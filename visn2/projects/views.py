# docs:
# function-based views: https://docs.djangoproject.com/en/3.2/topics/http/views/
# class-based views: https://docs.djangoproject.com/en/3.2/ref/class-based-views/
# classy class-based views: https://ccbv.co.uk/
import math
from email import message
from http import client
from os import name
from pyexpat import model
from re import search, template
#from aiohttp import request
#from cv2 import redirectError
from django.http import Http404
from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404

# from zmq import Message
from django.db.models import Q
from .forms import  NewProjForm, ProjFileForm
from .models import Project, Project, ProjFile #, MyUser, Messages
# from django.contrib.auth.models import User
from accounts.models import DjUser as User

from django.shortcuts import render

class ProjectsPageView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get('search_text')
        if self.request.user.userType == 1:
            projects = Project.objects.filter(client=self.request.user)
            if projects and search_text:
                projects = projects.filter(name__contains=search_text)
            context['projects'] = projects
        else:
            projects = Project.objects.filter(freelancer=self.request.user)
            if projects and search_text:
                projects = projects.filter(name__contains=search_text)
            context['projects'] = projects
        results = []
        for i in range(math.ceil(projects.count()/3)):
            results.append(projects[i * 3: (i+1) * 3])
        context['projects'] = results
        # context['target_users'] = get_chater(self.request.user)
        # context['form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            print('form valid success.')
            mto_name = form.cleaned_data.get('mto')
            mto_user = DjUser.objects.filter(username=mto_name).first()
            if not mto_user:
                return redirect(reverse_lazy('chat'))
            Message(mto=mto_user, msg=form.cleaned_data.get('message'), mfrom=request.user).save()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class ProjectsView(TemplateView):
    template_name = 'projects/projectv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.request.GET.get('id')
        if not project_id or not project_id.isdigit():
            raise Http404("Page is not found!")
        project = get_object_or_404(Project, pk=project_id)
        context['project'] = project
        # context['files'] = ProjFile.objects.filter(project=project)
        return context

class NewProjView(CreateView):
    template_name = 'projects/newproj.html'
    model = Project
    form_class = NewProjForm
    success_url = reverse_lazy('projects')
    


def projectsView(request):
    context = {}
    return render(request, 'projects/projects.html', context)

def singleProjectView(request):
    context = {}
    return render(request, 'projects/project.html', context)
