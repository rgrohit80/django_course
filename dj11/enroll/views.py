from django.shortcuts import render
from .forms import StudentForm
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
            # reg = Person(id=1, name=name, email=email, password=password)
            P1 = Person(name=name, email=email, password=password)
            P1.save()

    else:
        stu = StudentForm()
    return render(request, 'enroll/enroll.html', {'form': stu})
