from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos/crear/', views.crear_alumno, name = "crear_alumno"),
    path('alumnos/',views.listar_alumnos, name = "alumnos"),
    path('alumnos/<int:pk>/',views.DetalleAlumno.as_view(), name = "detalle_alumno"),
    path('alumnos/<int:pk>/modificar',views.ModificarAlumno.as_view(), name = "modificar_alumno"),
    path('alumnos/<int:pk>/eliminar',views.EliminarAlumno.as_view(), name = "eliminar_alumno") ,   
]
