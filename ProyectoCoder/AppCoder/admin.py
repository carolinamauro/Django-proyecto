from django.contrib import admin
#importo todos los modelos que queremos administrar y registrarlos en el archivo admin.py
from .models import * 

#registro cada una de mis tablas
admin.site.register(Curso) 
admin.site.register(Estudiante) 
admin.site.register(Profesor) 
admin.site.register(Entregable) 



