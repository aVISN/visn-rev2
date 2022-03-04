from django.urls import include,path
from . import views
from .views import DashboardView

urlpatterns = [
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('', views.dashboardView, name='dashboard'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('chat/', include('chat.urls', namespace='chat')),
]