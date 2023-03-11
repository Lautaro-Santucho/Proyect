from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    miFormulario=formularioContacto()

    if request.method=="POST":
        miFormulario=formularioContacto(data=request.POST)

        if miFormulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email= EmailMessage("Correo enviado desde django",
                               "Usuario: {}\nEmail: {} \n\n {}".format(nombre, email, contenido),
                               "", ["santucholautaro437@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?correcto")
            except:
                return redirect("/contacto/?incorrecto")

    return render(request, "Contacto/contacto.html", {"miFormulario":miFormulario})