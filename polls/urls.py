
from django.urls import path
from .views import db_interact, index, primer_template, template_raw, form_test

#Define la relacion entre una path y una view
urlpatterns = [
    path('index/', index, name='index'),
    path('template/', primer_template, name='primer_template'),
    path('template02/', template_raw, name='segundo template'),
    path('question/', db_interact, name='questions'),
    path('google/', form_test, name='google_form')
]