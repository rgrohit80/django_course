from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


#
# class Person(models.Model):
#     name = models.CharField(max_length=100, blank=True, verbose_name= "your Name")
#     email = models.EmailField(max_length=100, verbose_name='email add')
#     password = models.CharField(max_length=100, verbose_name="enter password", help_text="Enter complex password")

