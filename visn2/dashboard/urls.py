from django.urls import path
from . import views

urlpatterns = [
    path('',views.tempView, name='temp')
]