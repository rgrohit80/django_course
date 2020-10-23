from django.shortcuts import render
from django.views.generic import ListView
from .models import Student
from django.views.generic.detail import DetailView


# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'school/student.html'

    # def get_queryset(self):
    #     return Student.objects.exclude(name__in=['rohit', 'rahil'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'sonam':
    #         template_name = 'school/sonam.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = 'patna'
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'sonam':
    #         template_name = 'school/sonam.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]
