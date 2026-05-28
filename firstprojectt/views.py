from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from firstprojectt.models import Task
from firstprojectt.forms import TaskForm
from django.contrib import messages
# Create your views here.

def home(request):
    context = {
        'page' : "Home"
    }
    return render(request, "index.html", context)

def task(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task added successfully to the list")
            return redirect("task")
    all_task = Task.objects.all()
    context = {
        'page' : "Task",
        "all_task" : all_task,
    }
    return render(request, "task.html", context)

def aboutus(request):
    context = {
        'page' : "About"
    }
    return render(request, "about.html", context)

def contactus(request):
    context = {
        'page' : "Contact"
    }
    return render(request, "contact.html", context)
def address(request):
    context = {
        'page' : "Address"
    }
    return render(request, "address.html", context)