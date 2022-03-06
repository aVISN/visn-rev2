from django.urls import path
from . import views
# from .views import CustomLoginView

urlpatterns = [
    path('', views.projectsView, name='projects'),
    path('project/<int:project_id>/', views.singleProjectView, name='project'), #add ID here
    path('new_project/', views.createProjectView, name='create_project'),
    path('new_task/', views.addTask, name='new_task'),
]