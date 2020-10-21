from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        indexes = [
            models.Index(fields=['question_text'])
        ]

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Post(models.Model):
    post = models.CharField(max_length=100, default=' ')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post


class Candidate(models.Model):
    fname = models.CharField(max_length=50, blank=None, null=False, default="")
    lname = models.CharField(max_length=50, blank=None, null=False, default="")
    username = models.CharField(max_length=50, blank=None, default="")
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    zip_code = models.IntegerField()
    tnc = models.BooleanField(default=False)

    def __str__(self):
        return self.fname


class Address(models.Model):
    STATE = (
        ('', 'Choose'),
        ('MG', 'Minas Gerais'),
        ('SP', 'Sau paulo'),
        ('RJ', 'Rio De janerio')
    )
    email = models.EmailField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True, null=False)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100, choices=STATE)
    zip_code = models.CharField(max_length=100)
    check_me_out = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Application(models.Model):
    fname = models.CharField(max_length=200, null=False)
    lname = models.CharField(max_length=200, null=False)
    username = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
