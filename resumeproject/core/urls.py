from django.urls import path
from .views import home, contact, highlights

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('highlights/', highlights, name='highlights')
]
