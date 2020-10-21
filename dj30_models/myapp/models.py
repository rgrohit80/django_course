from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete


# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pagename = models.CharField(max_length=100)
    pagecat = models.CharField(max_length=100)
    pagedate = models.DateField()


