from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

    widgets = {
        'password': forms.PasswordInput(attrs={'required': True})
    }


class TeacherForm(StudentForm):
    teacher = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
