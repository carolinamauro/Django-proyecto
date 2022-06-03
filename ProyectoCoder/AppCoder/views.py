from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.template import loader
from AppCoder.forms import CursoFormulario,ProfesorFormulario


# Create your views here.

def curso(self):
    #creo mi objeto curso
    curso = Curso(nombre = "Desarrollo Web",camada= 16740) 
    curso.save()
    documento = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documento)

#son paginas
def profesores(request):
    return render(request,'AppCoder/profesores.html')

def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')

def entregables(request):
    return render(request,'AppCoder/entregables.html')

#tengo que tener un loader, que me carga la plantilla
def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cursoFormulario(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST) #me ññega toda la informacion del htmñ
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data #obtencion de datos
            curso = Curso(nombre = informacion['curso'],camada = informacion['camada'])
            curso.save()
            return render(request,'AppCoder/inicio.html')
    else:
        mi_formulario = CursoFormulario()
    return render(request,'AppCoder/cursoFormulario.html', {'mi_formulario': mi_formulario}) #pasamps por parametro el formulario para que sea usado


def profesorFormulario(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST) #me ññega toda la informacion del htmñ
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data #obtencion de datos
            profe = Profesor(nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'], profesion = informacion['profesion'])
            profe.save()
            return render(request,'AppCoder/inicio.html')
    else:
        mi_formulario = ProfesorFormulario()
    return render(request,'AppCoder/profesorFormulario.html', {'mi_formulario': mi_formulario}) #pasamps por parametro el formulario para que sea usado


def busquedaCamada(request):
    return render(request,'AppCoder/busquedaCamada.html') #especificamos el id a buscar 

def buscar(request):
  
    if request.GET['camada']:
        camada = request.GET['camada'] #lo que me pasan por id es el id del curso
        cursos = Curso.objects.filter(camada=camada)
        return render(request,'appCoder/resultadosBusqueda.html', {'cursos':cursos,'camada':camada}) #genero esta plantilla
    else:
        respuesta = "No se ha ingresado ninguna comision"
        return HttpResponse(respuesta)