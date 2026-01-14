from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello! This is my first Linux Mint Django page.</h1>")