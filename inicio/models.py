from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    dni = models.IntegerField()
    f_alta = models.DateField(default=date.today())
    comentarios = RichTextField(null=True)