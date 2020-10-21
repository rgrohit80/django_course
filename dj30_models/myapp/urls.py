from django.urls import path
from .views import index

urlpatterns = [
    path('app/', index, name='index')
]
