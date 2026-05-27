from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    context = {
        'page' : "Home"
    }
    return render(request, "index.html", context)

def task(request):
    context = {
        'page' : "Task"
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