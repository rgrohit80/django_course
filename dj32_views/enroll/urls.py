from django.urls import path
from .views import fview, Cview

urlpatterns = [
    path('fview1/', fview, {'template': 'enroll/home.html'}),
    path('fview2/', fview, {'template': 'enroll/office.html'}),
    path('cview1/', Cview.as_view(template_name='enroll/home.html')),
    path('cview2/', Cview.as_view(template_name='enroll/office.html'))
]
