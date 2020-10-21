from django.urls import path
from .views import index, detail, results, boot, save_post, show_post, spaceform, home, crispform, applicationform, \
    emailme, redbus, newpage

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:question_id>/', detail, name='detail'),
    path('result/<int:question_id>/', results, name='result'),
    path('boot/', boot, name='boot'),
    path('name/', save_post, name='save_post'),
    path('posts/', show_post, name='show_post'),
    path('spacex/', spaceform, name='spaceForm'),
    path('home/', home, name='home'),
    path('address/', crispform, name='crispform'),
    path('application/', applicationform, name='applicationform'),
    path('contact/', emailme, name='emailme'),
    path('redbus/', redbus, name='redbus'),
    path('apple/', newpage, name='newpage')
]
