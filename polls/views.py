from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Las views basadas en funciones siempre reciben un objeto request y contesta con un objeto HttpResponse
#signature: (request:Object --> HttpResponse)
def index(request):
    return HttpResponse('Hola Django, esta es la vista de index.')