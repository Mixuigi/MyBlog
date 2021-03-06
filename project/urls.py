from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.Authentication, name='registration'),
    path('', views.Home, name='Home_Page'),
    path('AddPosts/', views.FormPost, name='add_post '),
    re_path(r'(?P<POST>[-\w]+)/$', views.AddComment, name='add_comment'),
]
