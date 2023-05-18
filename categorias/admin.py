from django.contrib import admin
from categorias.models import MarcaImpresora, ModeloImpresora, TipoImpresora, ConectividadImpresora
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