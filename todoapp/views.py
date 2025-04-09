from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', 'PENDING')

        if title and description:
            Task.objects.create(title=title, description=description)
            return redirect('index')
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks':tasks})
def edit(request,id):
    task = get_object_or_404(Task,id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status','PENDING')
        task.save()
        return redirect('index')