from django.contrib import admin
from salida.models import VentaImpresora
# Register your models here.
class Ventas(admin.ModelAdmin):
    list_display = ('impresora','fecha','cantidad',)

admin.site.register(VentaImpresora,Ventas)