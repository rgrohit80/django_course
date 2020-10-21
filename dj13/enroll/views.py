from django.shortcuts import render
from .forms import StudentForm
from .models import Person
from django.http import HttpResponse
from .models import Person


# Create your views here.

def showform(request):
    if request.method == 'POST':
        # per = Person.objects.get(pk=1)
        stu = StudentForm(request.POST)
        if stu.is_valid():
            stu.save()

    else:
        stu = StudentForm()
    return render(request, 'enroll/enroll.html', {'form': stu})
