from django.urls import path
from .views import setsession, getsession, delsession

urlpatterns = [
    path('set/', setsession, name='setsession'),
    path('get/', getsession, name='getsession'),
    path('del/', delsession, name='delsession')
]
