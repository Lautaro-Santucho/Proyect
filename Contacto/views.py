from django.shortcuts import render
from .forms import formularioContacto

# Create your views here.

def contacto(request):
    miFormulario=formularioContacto()

    return render(request, "Contacto/contacto.html", {"miFormulario":miFormulario})