from django.shortcuts import render, redirect
from Tienda.models import Producto
from .carro import Carro

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro()
    produc= Producto.objects.get(id=producto_id)
    carro.agergarProducto(producto=produc)

    return redirect("/tienda/")

def restar_producto(request, producto_id):
    carro=Carro()
    produc= Producto.objects.get(id=producto_id)
    carro.restarProducto(producto=produc)

    return redirect("/tienda/")

def eliminar_producto(request, producto_id):
    carro=Carro()
    produc= Producto.objects.get(id=producto_id)
    carro.eliminar(producto=produc)

    return redirect("/tienda/")

def limpiar_carro(request, producto_id):
    carro=Carro()
    carro.limpiarCarro()

    return redirect("/tienda/")
