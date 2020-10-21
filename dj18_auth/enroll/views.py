from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages


# Create view with Usercreation extended form

def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "You have signed up successfully..!!")
    else:
        fm = SignUpForm()
        messages.info(request, "Please enter the details and proceed..")
    return render(request, 'enroll/sign_up.html', {'form': fm})


# Create your views here with Usercreation form.

def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'enroll/sign_up.html', {'form': fm})
