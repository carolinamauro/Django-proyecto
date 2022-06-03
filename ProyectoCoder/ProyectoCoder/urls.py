from django.contrib import admin
from django.urls import path,include
#from AppCoder.views import curso,inicio,profesores,estudiantes,entregables

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appCoder/',include('AppCoder.urls')),
    
]







