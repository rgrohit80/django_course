from django.shortcuts import render


# Create your views here.
def stu(request):
    return render(request, 'school/home.html')
