from django.contrib import admin
from .models import Producto,CategoriasProd
# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")    
admin.site.register(CategoriasProd,CategoriasAdmin)
admin.site.register(Producto,ProductoAdmin)