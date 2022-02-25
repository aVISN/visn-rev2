from django.urls import path
from . import views
# from .views import CustomLoginView

urlpatterns = [
    path('', views.projectsView, name='projects'),
    path('projects/project', views.singleProjectView, name='project'), #add ID here
    
]