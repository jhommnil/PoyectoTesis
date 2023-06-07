from django.contrib import admin
from categorias.models import MarcaImpresora, ModeloImpresora, TipoImpresora, ConectividadImpresora
from categorias.models import MarcaMonitor,ModeloMonitor,TipoMonitor,ConectividadMonitor
from categorias.models import MarcaTplink,ModeloTplink,TipoTplink,ConectividadTpelink
from categorias.models import MarcaTeclado,ModeloTeclado,TipoTeclado

# Register your models here.
class MarcaImpresoraAdmin(admin.ModelAdmin):
    list_display = ('marca',)
admin.site.register(MarcaImpresora, MarcaImpresoraAdmin)

class ModeloImpresoraAdmin(admin.ModelAdmin):
    list_display = ('modelo',)
admin.site.register(ModeloImpresora,ModeloImpresoraAdmin)

class TipoImpresoraAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
admin.site.register(TipoImpresora,TipoImpresoraAdmin)

class ConectividadImpresoraAdmin(admin.ModelAdmin):
    list_display = ('conectividad',)

admin.site.register(ConectividadImpresora,ConectividadImpresoraAdmin)

#Clases vista para Monitores

class MarcaMonitorAdmin(admin.ModelAdmin):
    list_display = ('marca',)
admin.site.register(MarcaMonitor,MarcaMonitorAdmin)

class ModeloMonitorAdmin(admin.ModelAdmin):
    list_display = ('modelo',)
admin.site.register(ModeloMonitor,ModeloMonitorAdmin)

class TipoMonitorAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
admin.site.register(TipoMonitor,TipoMonitorAdmin)

class ConectividadMonitorAdmin(admin.ModelAdmin):
    list_display = ('conectividad',)
admin.site.register(ConectividadMonitor,ConectividadMonitorAdmin)

# clases vista para tp-link

class MarcaTplinkAdmin(admin.ModelAdmin):
    list_display = ('marca',)
admin.site.register(MarcaTplink,MarcaTplinkAdmin)

class ModeloTplinkAdmin(admin.ModelAdmin):
    list_display = ('modelo',)
admin.site.register(ModeloTplink,ModeloTplinkAdmin)

class TipoTplinkAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
admin.site.register(TipoTplink,TipoTplinkAdmin)

class ConectividadTplinkAdmin(admin.ModelAdmin):
    list_display = ('conectividad',)
admin.site.register(ConectividadTpelink,ConectividadTplinkAdmin)

# clses vista para la tabla Teclado

class MarcaTecladoAdmin(admin.ModelAdmin):
    list_display = ('marca',)
admin.site.register(MarcaTeclado,MarcaTecladoAdmin)

class ModeloTecladoAdmin(admin.ModelAdmin):
    list_display = ('modelo',)
admin.site.register(ModeloTeclado,ModeloTecladoAdmin)

class TipoTecladoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
admin.site.register(TipoTeclado,TipoTecladoAdmin)