from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here. - ORM: Object Relational Mapper

# 1. Creas/Modificas/Eliminas un modelo (ORM)
# 2. Crear una migracion: makemigrations <nombre_app>
# 3. 

class Deudor(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    deuda = models.DecimalField(decimal_places=3, max_digits=50)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data_published')

    def __str__(self):
        return self.question_text