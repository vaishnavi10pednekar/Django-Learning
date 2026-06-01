from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    return HttpResponse("<h1>hello</h1>")
    register_form = UserCreationForm()
    return render(request, "register.html", {'register_form': register_form})

# Create your views here.
