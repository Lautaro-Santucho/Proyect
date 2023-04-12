from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from Pedidos.models import Pedidos, lineaPedidos
from carroCompras.carro import Carro


# Create your views here.

@login_required(login_url= "autenticacion/logear")
def procesar_pedido(request):
    pedido= Pedidos.object.create(user=request.user)
    carro= Carro(request)
    lineas_pedido=list()

    for key, value in carro.carro.items():
        lineas_pedido.append(lineaPedidos(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    lineaPedidos.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        linea_pedido=lineas_pedido,
        user_name=request.user.username,
        user_mail=request.user.email
    )
    messages.success(request, "El pedido se ha procesado con exito")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto= "Gracias por su compra"
    mensaje= render_to_string("email/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "linea_pedido": kwargs.get("linea_pedido"),
        "nombre_usuario": kwargs.get("user_name")       
    })

    mensaje_texto= strip_tags(mensaje) #quita las etiquetas html "<>"
    from_email= "santucholautaro437@gmail.com"
    to= kwargs.get("user_mail")
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

