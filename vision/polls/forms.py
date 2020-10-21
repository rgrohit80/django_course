from django import forms
from .models import Post, Candidate, Application


class PostForm(forms.ModelForm):
    post = forms.CharField(label='post', max_length=100)

    class Meta:
        model = Post
        fields = ('post',)


class CandidateForm(forms.ModelForm):
    fname = forms.CharField(label='candidate', max_length=100)

    class Meta:
        model = Candidate
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;'})
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Write here your message!'
    )


STATE = (
    ('', 'Choose'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sau paulo'),
    ('RJ', 'Rio De janerio')
)


class AddressForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 main st.'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATE)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'


class ContactmeForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=200, widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
