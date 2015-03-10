from django.conf.urls import patterns, include, url
from django.contrib import admin
import todoList.urls

urlpatterns = [
    
    url(r'^todoList/',include('todoList.urls')),
    url(r'^admin/', include(admin.site.urls)),
   
]
