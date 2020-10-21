from django.shortcuts import render
from django.views.generic.base import RedirectView


# Create your views here.

class MyredirectView(RedirectView):
    pattern_name = 'geek'
    permanent = True
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
