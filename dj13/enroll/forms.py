from django import forms
from django.core import validators
from .models import Person


class StudentForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'email', 'password']

        labels = {'name': "Enter name", 'email': "Enter Email", 'password': "Enter password"}
        widgets = {'password': forms.PasswordInput}
