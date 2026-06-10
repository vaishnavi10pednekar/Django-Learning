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
    return render(request, "edit_task.html", context)

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
    
    paginator = Paginator(con_info,5)
    page = request.GET.get("page")

    con_info = paginator.get_page(page)
        

    context = {
        'page' : "Contact",
        'con_info' : con_info
    }
    return render(request, "contact.html", context)

def del_con(request,data_id):
    con_obj = Contactt.objects.get(id=data_id)
    con_obj.delete()
    messages.success(request, "Contact info deleted successfully")
    return redirect("contactus")

def edit_con(request,data_id):
    con_obj = Contactt.objects.get(id=data_id)
    

    if request.method == "POST":
        form_data = ContacttForm(request.POST or None, instance=con_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Data updated successfully")
            return redirect("contactus")
        messages.success(request, "Invalid Updation")

    context = {
        "con_obj" : con_obj
    }
    return render(request,"edit_con.html", context)


def info(request):
    all_infor = Information.objects.all()
    if request.method == "POST":
        form_data = InformationForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Information added successfully")
            return redirect("info")
        messages.success(request, "Invalid Information")

    paginator = Paginator(all_infor,5)
    page = request.GET.get("page")

    all_infor = paginator.get_page(page)

    context = {
        'page' : "Information",
        'all_infor': all_infor,
    }
    return render(request, "info.html", context)

def del_info(request, data_id):
    del_inf = Information.objects.get(id=data_id)
    del_inf.delete()
    messages.success(request, "Information deleted successfully")
    return redirect("info")

def edit_info(request,data_id):
    edit_inf = Information.objects.get(id=data_id)

    if request.method == "POST":
        form_data = InformationForm(request.POST or None, instance = edit_inf)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Data updated successfully")
            return redirect("info")
        messages.success(request, "Invalid Updation")

    context = {
        "edit_inf" : edit_inf
    }
    return render(request,"edit_info.html", context)

