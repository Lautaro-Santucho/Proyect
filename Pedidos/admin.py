from django.contrib import admin
from .models import Pedidos, lineaPedidos

# Register your models here.

class pedidosAdmin(admin.ModelAdmin):
    readonly_fields=("created_at", )

class lineaPedidosAdmin(admin.ModelAdmin):
    readonly_fields=("created_at", )

admin.site.register(Pedidos, pedidosAdmin)
admin.site.register(lineaPedidos, lineaPedidosAdmin)