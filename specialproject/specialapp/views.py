from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'specialapp/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('home')
    return render(request, 'specialapp/add_task.html')
