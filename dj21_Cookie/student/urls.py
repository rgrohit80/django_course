from django.urls import path
from .views import set_cookie, get_cookie, del_cookie, set_sg_cookie, get_sg_cookie

urlpatterns = [
    path('set/', set_cookie, name='setcookie'),
    path('setsg/', set_sg_cookie, name='set_sg_cookie'),
    path('getsg/', get_sg_cookie, name='get_sg_cookie'),
    path('get/', get_cookie, name='getcookie'),
    path('del/', del_cookie, name='delcookie')
]
