from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


# Create your views here.

def home(request):
    print("i am view")
    return HttpResponse("I am view")


def excp(request):
    print("I am exception")
    a = 10 / 0
    return HttpResponse("This is exception page")


def user_info(request):
    print("I am user Info..!!")
    context = {'name': 'Rahul'}
    print(context['name'])
    return TemplateResponse(request, 'blog/user.html', context=context)
