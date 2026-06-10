from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    reg_form = UserCreationForm()
    context = {
        'page' : "Register",
        'reg_form' : reg_form,
    }
    return render(request, "register.html",context)
# Create your views here.
