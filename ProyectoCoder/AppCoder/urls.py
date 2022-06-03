from django.urls import path
from AppCoder import views

urlpatterns = [
    path('profesores/',views.profesores,name='Profesores'),
    path('curso/',views.curso, name='Curso'),
    path('inicio/',views.inicio, name='Inicio'),
    path('estudiantes/',views.estudiantes,name='Estudiantes'),
    path('entregables/',views.entregables,name='Entregables'),
    path('cursoFormulario/',views.cursoFormulario,name="CursoFormulario"),
    path('profesorFormulario/',views.profesorFormulario,name='ProfesoresForm'),
    path('busquedaCamada/',views.busquedaCamada,name="busquedaCamada"),
    path('buscar/',views.buscar,name="buscar"),
    
]

