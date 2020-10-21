from django.db import models
from datetime import datetime


# Create your models here.

class Technology(models.Model):
    tech = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')
    image = models.ImageField()
    about_me = models.TextField()
    experience = models.FloatField(default=0.0)
    technology = models.ManyToManyField(Technology)


class Project(models.Model):
    title = models.CharField(max_length=100)
    st_date = models.DateTimeField(default=datetime.now)
    ed_date = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
