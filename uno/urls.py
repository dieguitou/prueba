from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.IndexView.as_view(), name='hola'),
]
