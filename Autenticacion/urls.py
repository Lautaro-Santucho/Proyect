from django.urls import path
from .views import viewRegistro, cerrarSesion


urlpatterns = [
    path('', viewRegistro.as_view(), name="Autenticacion"),
    path('cerrarSesion', cerrarSesion, name="cerrar_sesion"),

]