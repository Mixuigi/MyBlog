from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='posts'),
    path('AddPosts/', views.FormPost, name='add_post '),
    path('AddComments/', views.FormCommens, name='add_comments')
]
