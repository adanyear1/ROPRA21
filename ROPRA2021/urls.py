"""
Definition of urls for ROPRA2021.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/whatisautomation', views.whatisauto, name='whatisautomation'),
]
