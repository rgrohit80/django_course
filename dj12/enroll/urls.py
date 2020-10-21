from django.urls import path
from .views import showform, showsimple

urlpatterns = [
    path('', showform, name='showform'),
    path('simple/', showsimple)
]
