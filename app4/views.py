from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app4(requerst):
    return HttpResponse('<h1>app4 views</h1>')
