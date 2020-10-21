from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class Tview(TemplateView):
    template_name = 'enroll/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'rohit'
        context['age'] = 30
        return context
