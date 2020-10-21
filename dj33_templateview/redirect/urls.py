from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from .views import MyredirectView

urlpatterns = [
    path('', TemplateView.as_view(template_name='redirect/index.html'), name='home'),
    path('index/', RedirectView.as_view(pattern_name='home')),
    path('home/<slug:post>/', TemplateView.as_view(template_name='redirect/index.html'), name='geek'),
    path('<slug:post>/', MyredirectView.as_view())

]
