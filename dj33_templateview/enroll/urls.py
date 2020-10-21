from django.urls import path
from .views import Tview

urlpatterns = [
    path('tview/', Tview.as_view(), name='tview')
]
