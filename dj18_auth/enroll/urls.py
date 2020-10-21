from django.urls import path
from .views import sign_up, signup

urlpatterns = [
    path('sign_up/', signup, name='sign_up'),
    path('signup/', sign_up, name='signup')
]
