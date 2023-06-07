from django.contrib import admin
from salida.models import VentaImpresora,VentaMonitor,VentaTplink,VentaTeclado
# Register your models here.
class Ventas(admin.ModelAdmin):
    list_display = ('impresora','fecha','cantidad',)

admin.site.register(VentaImpresora,Ventas)

class VentaMonitorAdmin(admin.ModelAdmin):
    list_display = ('monitor','fecha','cantidad',)
admin.site.register(VentaMonitor,VentaMonitorAdmin)

class VentaTplinkAdmin(admin.ModelAdmin):
    list_display = ('tplink','fecha','cantidad',)
admin.site.register(VentaTplink,VentaTplinkAdmin)

class VentaTecladoAdmin(admin.ModelAdmin):
    list_display = ('teclado','fecha','cantidad',)

admin.site.register(VentaTeclado,VentaTecladoAdmin)