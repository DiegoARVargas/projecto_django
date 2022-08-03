from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here. - ORM: Object Relational Mapper

# 1. Creas/Modificas/Eliminas un modelo (ORM)
# 2. Crear una migracion: makemigrations <nombre_app>
# 3. Aplicas los cambios en la base de datos: migrate <nombre_app>

# Django automaticamente define el nombre de la tabla como: <appanme>_<classname> todo en minuscula
# 3. Las instancias definen los modelos y representan registros en la tabla.
# 4. Posibilita la consulta en la base de datos atravez de un MANAGER, atributo, objects

class Deudor(models.Model): 
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    deuda = models.DecimalField(decimal_places=3, max_digits=50)
    data_de_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data_published')

    def __str__(self):
        return self.question_text