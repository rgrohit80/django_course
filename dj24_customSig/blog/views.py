from django.shortcuts import render
from . import signals
from django.http import HttpResponse


# Create your views here.

def home(request):
    signals.notification.send(sender=None, request=request, user=['Geeky', 'Shows'], name="Rohit")
    return HttpResponse("This is home page..!")
