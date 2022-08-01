from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

#importamos los modelos (clase Question) de los polls/models.py
from polls.models import Question

# Create your views here.

#Las views basadas en funciones siempre reciben un objeto request y contesta con un objeto HttpResponse
#signature: (request:Object --> HttpResponse)
def index(request):
    return HttpResponse('Hola Django, esta es la vista de index.')

def primer_template(request): # El template de Django es server rendering, es decir que se ejecuta en el servidor
    kiko = 'valor'
    valores = ('verde', 'azul', 'amarillo', 'rojo')
    return render(
        request, 
        template_name='polls/index.html', 
        context={'name': kiko, 'colores': valores}
    )


# Demostramos como funciona eñ shortcuts "render"
from django.template import loader

def template_raw(request):
    kiko = 'valor'
    valores = ('verde', 'azul', 'amarillo', 'rojo')
    respuesta = loader.render_to_string(
        request = request,
        template_name='polls/index.html', 
        context={'name': kiko, 'colores': valores}
    )
    return HttpResponse(respuesta)

def db_interact(request):
    questions = Question.objects.all()
    return render(
        request=request,
        template_name='polls/question.html',
        context={'questions': questions}
    )   
