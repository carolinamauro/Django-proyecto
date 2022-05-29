from django.contrib import admin
from django.urls import path
#importo la funcion para poder usarla
from Proyecto1.views import saludo, DiaDeHoy, nombre_persona, probandoTemplates


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('DiaDeHoy/',DiaDeHoy),
    #especificar la informacion, le paso un argumento que tiene que usar para su logica
    path('nombre_persona/<nombre>/', nombre_persona), 
    path('probandoTemplate/', probandoTemplates),
]

