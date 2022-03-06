from django.urls import path
from . import views
# from .views import CustomLoginView

urlpatterns = [
    path('', views.contactsView, name='contacts'),
]