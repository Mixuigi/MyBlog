from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/', include('project.urls')),
    path('', include('project.urls')),
    url(r'^project/', include(('project.urls', 'project'),
                              namespace='project', ), )
]
