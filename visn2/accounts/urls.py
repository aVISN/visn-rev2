from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('login/success', views.postLoginView, name='successLogin'),

]