from django.shortcuts import render
from inicio.forms import CrearAlumnoFormulario, BuscarAlumnoFormulario 
from inicio.models import Alumno
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def crear_alumno(request):
    mensaje = ''    
    if request.method == "POST":
        formulario = CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(nombre = info['nombre'],apellido = info['apellido'], edad=info['edad'], dni=info['dni'])
            alumno.save()
            mensaje = f'Se dio de alta a {alumno.nombre} como alumno'
        else:
            return render(request, 'inicio/crear_alumno.html', {'formulario' : formulario})
                    
    formulario = CrearAlumnoFormulario()
    return render(request, 'inicio/crear_alumno.html', {'formulario' : formulario, 'mensaje':mensaje})

def listar_alumnos(request):
    formulario = BuscarAlumnoFormulario(request.GET)
    listado = []
    if formulario.is_valid():
        busqueda = formulario.cleaned_data["dni"]
        listado = Alumno.objects.filter(dni__contains=str(busqueda))
    else:
        print("DNI Not Found")
    
    formulario = BuscarAlumnoFormulario()    
    return render(request, 'inicio/listar_alumnos.html',{'formulario':formulario, "alumnos":listado})


class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "inicio/detalle_alumno.html"


class ModificarAlumno(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = ["nombre","apellido","edad","dni"]
    template_name = "inicio/modificar_alumno.html"
    success_url= reverse_lazy("inicio:alumnos")


class EliminarAlumno(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = "inicio/eliminar_alumno.html"
    success_url= reverse_lazy("inicio:alumnos")
