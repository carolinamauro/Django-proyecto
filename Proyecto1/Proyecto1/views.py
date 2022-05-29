from unittest import result
from django.http import HttpResponse
import datetime
from django.template import Template,Context, loader

def saludo(request):
    return HttpResponse('Hola Django - Coder')

def DiaDeHoy(request):
    #informacion de este momento den particular
    dia = datetime.datetime.now() 
    texto = 'Hoy es: {}'.format(dia)
    return HttpResponse(texto)

def nombre_persona(self,nombre):
    resultado = "Mi nombre es: <br> <br> {}".format(nombre)
    return HttpResponse(resultado)

def probandoTemplates(self):

    nombre = 'Carolina'
    apellido = 'Mauro'
    listaDeNotas = [2,5,7,3]

    diccionario = {"nombre": nombre, "apellido": apellido,"listaDeNotas": listaDeNotas}
    #miHtml = open('template1.html') 

   # plantilla = Template(miHtml.read()) 

    #miHtml.close() 
    #puente entre mi views y mi Html
   # miContexto = Context(diccionario) # le permito a mi Html utilizar estas variables 
	
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario) #me permite acceder al template

    return HttpResponse(documento)

    