from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse


# Create your views here.
def setsession(request):
    request.session['name'] = 'lukas'
    return render(request, 'student/setsession.html')


def getsession(request):
    if 'name' in request.session:
        name = request.session.get('name')
        item = request.session.items()
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name': name, 'item': item})
    else:
        return HttpResponse("Your session has expired")


def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')
