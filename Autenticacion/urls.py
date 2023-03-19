from django.urls import path
from .views import viewRegistro


urlpatterns = [
    path('', viewRegistro.as_view(), name="Autenticacion"),

]