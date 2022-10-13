import datetime
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers

# TODO: Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist_item = Task.objects.filter(user=request.user)
    context = {"list_item": data_todolist_item, "username": request.user}
    
    return render(request, 'todolist.html',context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def new_task(request):
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        Task.objects.create(user = request.user,date = datetime.datetime.now(),title = request.POST.get('title'),description = request.POST.get('description'),)
        return response
    context = {}
    return render(request, 'new_task.html',context)

def update_task(request, id):
    task = Task.objects.get(pk=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return HttpResponseRedirect("/todolist/")

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect("/todolist/")


# Assignment 6
@login_required(login_url="/todolist/login")
def show_todolist_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', tasks), content_type='application/json')

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = Task(user=request.user, title=title, description=description, date=datetime.now())
        new_task.save()
    return HttpResponse('')