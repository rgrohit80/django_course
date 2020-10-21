from django.shortcuts import render
from .models import Student


# Create your views here.
def student(request):
    stu = Student.student.roll_range(200, 300)
    return render(request, 'student/home.html', {'students': stu})
