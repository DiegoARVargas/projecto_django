
from django.urls import path
from .views import index

#Define la relacion entre una path y una view
urlpatterns = [
    path('index/', index, name='index')
]