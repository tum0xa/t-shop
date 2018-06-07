from django.urls import path, include
from . import views

urlpatterns = [
                  path('register', views.register, name='register'),
                  path('activate/', views.activate, name='activate'),
              ]
