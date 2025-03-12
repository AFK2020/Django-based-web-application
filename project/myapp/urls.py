from django.urls import path
from . import views

urlpatterns = [
    path('get-ip/', views.get_user_ip, name='get_ip'),
]