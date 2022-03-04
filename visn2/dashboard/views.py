import math
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, FormView

from projects.models import Project, Project, ProjFile
from projects.views import ProjectsPageView

class DashboardView(ProjectsPageView,TemplateView):
    template_name = 'dashboard/dashboard.html'
