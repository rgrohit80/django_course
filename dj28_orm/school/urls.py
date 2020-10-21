from django.urls import path
from .views import stu

urlpatterns = [
    path('stu/', stu, name='stu')
]
