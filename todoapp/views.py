from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('desccription')
        status = request.POST.get('status', 'PENDING')

        if title and description:
            Task.objects.create(title=title, description=description)
            return redirect('index')
        tasks = Task.objects.all()
    return render(request, "index.html", {'tasks':tasks})