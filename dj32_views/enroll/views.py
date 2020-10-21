from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.

def fview(request, template):
    return render(request, template)


class Cview(View):
    template_name = ''

    def get(self, request):
        return render(request, self.template_name)

