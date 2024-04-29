from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    # return HttpResponse("<h1>FIRST TEST</h1>")
    return render(response, "index.html")
 

def v1(response):
    return HttpResponse("<h1>THIS IS DIFFERENT</h1>")
