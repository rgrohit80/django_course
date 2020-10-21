from django.urls import path
from .views import sign_up, signup, user_login, user_profile, user_logout, user_change_pass, user_detail

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', user_login, name='user_login'),
    path('profile/', user_profile, name='user_profile'),
    path('logout/', user_logout, name='user_logout'),
    path('changepass/', user_change_pass, name='changepass'),
    path('userdetail/<int:id>/', user_detail, name='userdetail')
]
