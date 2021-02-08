from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='posts'),
    path('', views.FormComments, name='add_comments'),
    path('AddPosts/', views.FormPost, name='add_post '),
    # path('AddComments/', views.FormComments, name='add_comments')
]
