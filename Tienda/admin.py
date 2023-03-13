from django.contrib import admin
from .models import categoriaProducto, Producto

# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields= ("created", "updated")

class productosAdmin(admin.ModelAdmin):
    readonly_fields= ("created", "updated")

admin.site.register(categoriaProducto, categoriaAdmin)
admin.site.register(Producto, productosAdmin)