from django.contrib import admin
from Stock.models import Impresoras,Monitor,Tplink,Teclado
# Register your models here.
class ImpresoraAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','tipo','conectividad','precio_venta','cantidad','fecha_registro','estado',)
admin.site.register(Impresoras,ImpresoraAdmin)

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','tipo_pantalla','conectividad','fecha_registro','precio_venta','estado','cantidad',)
admin.site.register(Monitor,MonitorAdmin)

class TplinkAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','tipo','conectividad','fecha_registro','precio_venta','estado','cantidad',)
admin.site.register(Tplink,TplinkAdmin)

class TecladoAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','tipo','fecha_registro','precio_venta','estado','cantidad',)

admin.site.register(Teclado,TecladoAdmin)