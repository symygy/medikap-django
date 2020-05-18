from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board, name ='summary'),
]