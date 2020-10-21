from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddShowView.as_view(), name='addshow'),
    path('delete/<int:id>/', views.DeleteData.as_view(), name='delete_data'),
    path('update/<int:id>/', views.UpdateData.as_view(), name='update_data')
]
