from django import forms
from django.core import validators
from .models import Person


class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Person
        fields = ['name', 'email', 'password']

        labels = {'name': "Enter name", 'email': "Enter Email", 'password': "Enter password"}
        error_messages = {'name': {'required': "nam kikhna zaroori hai"},
                          'email': {'required': "password likhna bhi zaroori hain"}}
        widgets = {'password': forms.PasswordInput,
                   'name': forms.TextInput(attrs={'class': "myclass", 'placeholder': "yahan nam likhen",
                                                  'style': "color:red;"})}


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.FileInput,
        choices=FAVORITE_COLORS_CHOICES,
    )
