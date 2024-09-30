# complaints/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_complaint, name='submit_complaint'),
     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]