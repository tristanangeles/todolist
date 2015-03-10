#!/usr/bin/env python

from django.conf.urls import patterns, include, url
from todoList import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<task_id>\d+)/$',views.detail,name='detail'),
    url(r'^new',views.new_task,name='new'),
    url(r'^add',views.add_task,name='add')
    
    
    
    
]
