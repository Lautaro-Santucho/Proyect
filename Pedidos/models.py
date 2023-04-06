from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import Sum, F, FloatField

# Create your models here.

User= get_user_model()

class Pedidos(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
    
        Sum(F("precio")*F("cantidad"), output_field= FloatField())

        )["total"]

    class Meta:
        db_table= "Pedidos"
        verbose_name= "Pedido"
        verbose_name_plural= "Pedidos"
        ordering= ["id"]

class lineaPedidos(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id= models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedidos_id= models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cantidad= models.IntegerField(default=1)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Producto: {self.producto_id.nombre} Cantidad: {self.cantidad}"
    
    class Meta:
        db_table= "lineaPedidos"
        verbose_name= "Linea Pedido"
        verbose_name_plural= "Lineas Pedidos"
        ordering= ["id"]