from django.urls import path
from .views import regi

urlpatterns = [
    path('', regi, name='regi')
]
