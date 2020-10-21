from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    data = {'name': 'rohit', 'city': 'DehriOnSone'}
    return HttpResponse(data['name'] + '' + data['city'])
