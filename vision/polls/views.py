"""This module does blah blah."""

from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Post, Address, Application
from django.shortcuts import render
from .forms import PostForm, CandidateForm, ContactForm, AddressForm, ApplicationForm, ContactmeForm

from django.core.mail import send_mail
from django.db import transaction


# Create your views here.
@transaction.atomic
def index(request):
    """This is index method."""
    latest_question_list = Question.objects.all()
    context = {'questions': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """This is detail method."""
    question = Question.objects.get(id=question_id)
    return HttpResponse("you are looking at question called ' {} '?".format(question.question_text))


def results(request, question_id):
    """This is result method."""
    return HttpResponse("you are looking at the result of the question {}".format(question_id))


def boot(request):
    """This is boot method."""
    return render(request, 'polls/boot.html')


def save_post(request):
    """This is save_post method."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/polls/posts/')
    else:
        form = PostForm()
    return render(request, 'polls/name.html', context={'form': form})


def show_post(request):
    """This is show post method."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'polls/posts.html', context)


def spaceform(request):
    """This is spacerform method."""
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<p> Form saved</p>")
    else:
        form = CandidateForm()
        return render(request, 'polls/spacex.html', {'form': form})


def home(request):
    """This is home method."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
        return render(request, 'polls/home.html', {'form': form})


def crispform(request):
    """This is crispForm method."""
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            addr = Address()
            addr.email = form.cleaned_data['email']
            addr.password = form.cleaned_data['password']
            addr.address1 = form.cleaned_data['address1']
            addr.address2 = form.cleaned_data['address2']
            addr.city = form.cleaned_data['city']
            addr.state = form.cleaned_data['state']
            addr.zip_code = form.cleaned_data['zip_code']
            addr.check_me_out = form.cleaned_data['check_me_out']
            addr.save()
            return HttpResponseRedirect('/polls/address/')
    else:
        form = AddressForm()
    return render(request, 'polls/address.html', {'form': form})


def applicationform(request):
    """This is application method."""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/polls/application/')
        else:
            form = ApplicationForm()
    form = ApplicationForm()
    context_data = {'form': form}
    return render(request, 'polls/spacex.html', {'form': form})


def emailme(request):
    """This is email method."""
    if request.method == 'POST':
        form = ContactmeForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipient = ['rgrohit81@gmail.com']
            if cc_myself:
                recipient.append(sender)
            send_mail(subject, message, sender, recipient)
            return HttpResponse("<p>Thanks</p>")
    form = ContactmeForm()
    return render(request, 'polls/contactme.html', {'form': form})


def redbus(request):
    return render(request, 'polls/redbus.html')


def newpage(request):
    prod = {'name': ['rohit', 'frans', 'zoman', 'roman'], 'country': 'Armenia'}
    return render(request, 'polls/apple.html', prod)
