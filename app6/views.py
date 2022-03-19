from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app6(requerst):
    return HttpResponse('<h1>app6 views</h1>')
