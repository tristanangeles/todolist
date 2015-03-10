from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from .models import Task
# Create your views here.

def index(request):
    
    task_list=Task.objects.all()
    
    return render(request,'todoList/index.html',{'tasks':task_list})


def detail(request,task_id):
    
    
    task=get_object_or_404(Task,pk=task_id)
    
    return render(request,'todoList/detail.html',{'task':task})


def new_task(request):
    
    return render(request,'todoList/new.html')


def add_task(request):
    
    new_task=Task(title=request.POST.get("title"),description=request.POST.get("description"),start=datetime.now(),deadline=datetime.now())
    new_task.save()
    
    task_list=Task.objects.all()
    
    return render(request,'todoList/index.html',{'tasks':task_list})
    
