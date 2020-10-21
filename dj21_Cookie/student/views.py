from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.

def set_cookie(request):
    response = render(request, 'student/setsession.html')
    response.set_cookie('name', 'rohit', expires=datetime.utcnow() + timedelta(days=2))
    return response


def set_sg_cookie(request):
    response = render(request, 'student/setsession.html')
    response.set_signed_cookie('name', 'rohit', salt='nm', expires=datetime.utcnow() + timedelta(days=2))
    return response


def get_cookie(request):
    name = request.COOKIES.get('name', 'default')
    return render(request, 'student/getsession.html', {'name': name})


def get_sg_cookie(request):
    name = request.get_signed_cookie('name', salt='nm')
    return render(request, 'student/getsession.html', {'name': name})


def del_cookie(request):
    response = render(request, 'student/delsession.html')
    response.delete_cookie('name')
    return response
