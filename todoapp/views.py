from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks':tasks})