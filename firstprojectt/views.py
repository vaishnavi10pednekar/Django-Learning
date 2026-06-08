from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from firstprojectt.models import Task
from firstprojectt.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from firstprojectt.models import Information
from firstprojectt.forms import InformationForm
from firstprojectt.models import Contactt
from firstprojectt.forms import ContacttForm
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
    paginator = Paginator(all_task,5)
    page = request.GET.get("page")

    all_task = paginator.get_page(page)

    context = {
        'page' : "Task",
        "all_task" : all_task,
    }
    return render(request, "task.html", context)

def del_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    task_obj.delete()
    messages.success(request, "Task deleted successfully from the list")
    return redirect("task")

def edit_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    if request.method == "POST":
        form_data = TaskForm(request.POST or None, instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task updated successfully to the list")
            return redirect("task")
        

    context = {
        'task_obj' : task_obj
    }
    return render(request, "edit.html", context)

def comp_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request, "Complete Status Updated")
    return redirect("task")

def pend_task(request, task_id):
    task_obj = Task.objects.get(id = task_id)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request, "Complete Status Updated")
    return redirect("task")

def aboutus(request):
    context = {
        'page' : "About"
    }
    return render(request, "about.html", context)

def contactus(request):
    con_info = Contactt.objects.all()
    if request.method == "POST":
        form_data = ContacttForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Data added successfully")
            return redirect("contactus")
        messages.success(request, "Invalid Data")
        

    context = {
        'page' : "Contact",
        'con_info' : con_info
    }
    return render(request, "contact.html", context)

def info(request):
    all_infor = Information.objects.all()
    if request.method == "POST":
        form_data = InformationForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Information added successfully")
            return redirect("info")
        messages.success(request, "Invalid Information")
    context = {
        'page' : "Information",
        'all_infor': all_infor,
    }
    return render(request, "info.html", context)


