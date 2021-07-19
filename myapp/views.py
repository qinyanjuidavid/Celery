from django.shortcuts import render
from django.http import HttpResponse
from myapp.tasks import Sleepy

def index(request):
    Sleepy(10)
    return HttpResponse("<h1>Done</h1>")
