from django.urls import path
from . import views
# from .views import CustomLoginView

from .views import ProjectsPageView, NewProjView, ProjectsView
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
    path('project/', views.singleProjectView, name='project'), #add ID here
    path('newproj/', NewProjView.as_view(), name='newproj'),
    path('projectv/', ProjectsView.as_view(), name='projectv'),
]