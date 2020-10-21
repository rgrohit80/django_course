from django.urls import path
from .views import showformdata

urlpatterns = [
    path('', showformdata, name='showformdata')
]
