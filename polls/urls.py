
from django.urls import path
from .views import index, primer_template

#Define la relacion entre una path y una view
urlpatterns = [
    path('index/', index, name='index'),
    path('template/', primer_template, name='primer_template')
]