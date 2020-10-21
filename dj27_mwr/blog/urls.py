from django.urls import path
from .views import home, excp, user_info

urlpatterns = [
    path('home/', home, name='home'),
    path('excp/', excp, name='excp'),
    path('user_info', user_info, name='user_info')
]
