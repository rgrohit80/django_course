from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Portform


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Portform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("khsakf")
        else:
            form = Portform()
    form = Portform()
    context_data = {'form': form}
    return render(request, 'portfolio/portfolio.html', {'form': form})


def home(request):
    return render(request, 'portfolio/dbcache.html')
