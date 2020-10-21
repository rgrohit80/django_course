from django.contrib import admin
from .models import Question, Choice, Address, Application

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Address)
admin.site.register(Application)
