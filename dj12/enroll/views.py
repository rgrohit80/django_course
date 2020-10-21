from django.shortcuts import render
from .forms import StudentForm, SimpleForm
from django.http import HttpResponse
from .models import Person


# Create your views here.

def showform(request):
    if request.method == 'POST':
        stu = StudentForm(request.POST)
        if stu.is_valid():
            name = stu.cleaned_data['name']
            email = stu.cleaned_data['email']
            password = stu.cleaned_data['password']
            print(name)
            print(email)
            print(password)

    else:
        stu = StudentForm()
    return render(request, 'enroll/enroll.html', {'form': stu})


def showsimple(request):
    stu = SimpleForm(request.POST)
    return render(request, 'enroll/enroll.html', {'form': stu})
