from django import forms
from ckeditor.fields import RichTextFormField

class CrearAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    dni = forms.IntegerField()
    f_alta = forms.DateField()
    comentarios=RichTextFormField()
    
class BuscarAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20,required=False)