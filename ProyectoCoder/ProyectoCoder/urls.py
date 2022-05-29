from django.contrib import admin
from django.urls import path
from AppCoder.views import curso,mi_plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso/',curso),
    path('mi_plantilla/',mi_plantilla)
]

