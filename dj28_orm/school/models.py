from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()


class Student_proxy(Student):
    class Meta:
        proxy = True;
