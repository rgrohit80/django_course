from django.shortcuts import render
from .forms import StudentForm, TeacherForm


# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm1 = StudentForm(request.POST)
        fm2 = TeacherForm(request.POST)
        if fm1.is_valid() and fm2.is_valid():
            print(fm1.cleaned_data.get('name'))
            print(fm2.cleaned_data.get('name'))
            print(fm2.cleaned_data.get('teacher'))
            fm1 = StudentForm()
            fm2 = TeacherForm()
    else:
        fm1 = StudentForm()
        fm2 = TeacherForm()
    return render(request, 'enroll/showdata.html', {'form1': fm1, 'form2': fm2})
