from django import forms


# def starts_with_s(value):
#     if value[0] != 's':
#         raise forms.ValidationError('the name should start from s')

class StudentForm(forms.Form):
    name = forms.CharField(error_messages={'required': "Enter your name"})
    email = forms.EmailField(error_messages={'required': "Enter your email"})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': "Enter your password"})

"""
form validation as below
"""

"""

    def clean(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        passwd = self.cleaned_data['password']

        if name == 'rohit' and email == 'rg@gmail.com' and len(passwd) > 6:
            return
        else:
            raise forms.ValidationError("Please enter the correct value..!!")

    def clean_name(self):
        data = self.cleaned_data['name']
        if data == 'saket':
            return data
        raise forms.ValidationError("Please enter value Saket..!")

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        if cleaned_data.get('password') != cleaned_data.get('repassword'):
            raise forms.ValidationError("Password does not match")

    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data.get('name')
        if len(valname) < 5:
            raise forms.ValidationError("Char should be more than 5")
        valemail = cleaned_data.get('email')
        if len(valemail) > 100:
            raise forms.ValidationError("Enter proper email id")

    def clean_name(self):
        val = self.cleaned_data.get('name')
        if len(val) < 5:
            raise forms.ValidationError("Enter more that 5 charactor")
        return val

"""