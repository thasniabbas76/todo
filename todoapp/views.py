from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Task, User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', 'PENDING')

        if title and description:
            Task.objects.create(title=title, description=description, status=status)
            return redirect('index')
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks':tasks})
def edit(request,id):
    task = get_object_or_404(Task,id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()
        return redirect('index')
    return render(request, 'edit.html',{'task':task})
def delete(request,id):
    task = get_object_or_404(Task,id = id)
    task.delete()
    return redirect('index')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid credentials.")

    return render(request, 'login.html')
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if name and email and password:
            if User.objects.filter(email=email).exists():
                return HttpResponse("Email already exists.")
            else:
                User.objects.create_user(name=name,email=email,password=password)
                return redirect('login')
    
    return render(request, 'signup.html')
def logout_view(request):
    logout(request)
    return redirect('login')