from django.urls import path
from .views import StudentListView, StudentDetailView

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='studentdetail')
]
