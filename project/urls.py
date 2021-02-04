from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/', views.index, name='index'),
    path('', views.FormPost)
]
