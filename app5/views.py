from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app5(requerest):
    return HttpResponse('<h1>app5 viewe<>/h1')
    
