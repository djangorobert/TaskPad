from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy
from django.utils import timezone
#Import the generic views here
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class TaskCreate(CreateView):
	model = Task
	fields = ['name']
	success_url = reverse_lazy('tasklist:task_list')
class TaskUpdate(UpdateView):
	model = Task
	fields = ['name']
	success_url = reverse_lazy('tasklist:task_list')
	
class TaskDelete(DeleteView):
	model = Task
	success_url = reverse_lazy('tasklist:task_list')
	
class TaskList(ListView):
	model = Task
