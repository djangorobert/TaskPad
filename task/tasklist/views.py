from django.shortcuts import render
from .models import Task, Customer
from django.urls import reverse_lazy
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
#for the functional views authentication
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

#Import the generic views here
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Task
    fields = ['name']
    success_url = reverse_lazy('tasklist:task_list')
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
class TaskUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Task
    fields = ['name']
    success_url = reverse_lazy('tasklist:task_list')
	
class TaskDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Task
    success_url = reverse_lazy('tasklist:task_list')
	
class TaskList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Task
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = Task.objects.filter(user_name=self.request.user)
        return context
   
    
   


#Authentican Views to Login, Logout, Signup(Register)
#The Custom Login and Logout Views
def login_view(request):
    next = request.GET.get('next') #/premium/
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            messages.info(request, 'Succesfully Logged in.')
            if next:
                return redirect(next)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, "tasklist/login.html", context)

def logout(request):
    return render(request, 'tasklist/logout.html')

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=user.username, password=password)
            login(request, auth_user)
            messages.info(request, 'Succesfully registered')
            if next:
                return redirect(next)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'tasklist/signup.html', context)

def about(request):
    return render(request, 'tasklist/about.html')


@login_required
def profile(request):
    

    last_task_added = Task.objects.filter(user_name=request.user).last()
    #users_mileage = Mileage.objects.filter(user_name=request.user).aggregate(Sum('miles'))
    only_users_tasks = Task.objects.filter(user_name=request.user)
    newest_tasks = Task.objects.filter(user_name=request.user, timestamp__gte=datetime.now()-timedelta(hours=1))

    context = {
        
        'last_task_added': last_task_added,
        'only_users_tasks': only_users_tasks,
        'newest_tasks': newest_tasks,
    }
    return render(request, 'tasklist/profile.html', context)