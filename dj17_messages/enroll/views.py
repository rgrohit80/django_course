from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages


# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your account has been created..!!")
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
        messages.set_level(request, messages.DEBUG)
        messages.info(request, "Enter you details here..!!")
        messages.info(request, "this is info messages..")
        messages.success(request, "This is success messages")
        messages.error(request, "This is error page")
        messages.debug(request, "this is debug messages")
        print(messages.get_level(request))
    return render(request, 'enroll/userregistration.html', {'form': fm})
