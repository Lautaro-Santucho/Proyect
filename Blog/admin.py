from django.contrib import admin
from .models import Categorias, Post

# Register your models here.

class categoriasAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class postAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(Categorias, categoriasAdmin)
admin.site.register(Post, postAdmin)