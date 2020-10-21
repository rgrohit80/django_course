from django.urls import path
from .views import showform

urlpatterns = [
    path('', showform, name='showform')
]
