from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        linea_pedid=lineas_pedido,
        username=request.username,
        usermail=request.usermail
    )
    messages.success(request, "El pedido se ha procesado con exito")

    return redirect("../tienda")

def enviar_mail(request):
    pass
