from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    print("i am view")
    return HttpResponse("I am view")
