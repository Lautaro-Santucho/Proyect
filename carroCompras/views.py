from django.shortcuts import render, redirect
from Tienda.models import Producto
from .carro import Carro

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro(request)
    produc= Producto.objects.get(id=producto_id)
    carro.agergarProducto(producto=produc)

    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    produc= Producto.objects.get(id=producto_id)
    carro.restarProducto(producto=produc)

    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    produc= Producto.objects.get(id=producto_id)
    carro.eliminar(producto=produc)

    return redirect("Tienda")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiarCarro()

    return redirect("Tienda")
