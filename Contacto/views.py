from django.shortcuts import render, redirect
from .forms import formularioContacto

# Create your views here.

def contacto(request):
    miFormulario=formularioContacto()

    if request.method=="POST":
        miFormulario=formularioContacto(data=request.POST)

        if miFormulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/contacto/?correcto")

    return render(request, "Contacto/contacto.html", {"miFormulario":miFormulario})