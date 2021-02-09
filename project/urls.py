from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.Registration, name='registration'),
    # path('registration/', views.Registration, name='registration'),
    path('', views.Home, name='Home_Page'),
    path('AddPosts/', views.FormPost, name='add_post '),
]
