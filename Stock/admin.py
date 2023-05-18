from django.contrib import admin
from Stock.models import Impresoras
# Register your models here.
class ImpresoraAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','conectividad','precio_venta','cantidad','fecha_registro','estado',)
admin.site.register(Impresoras,ImpresoraAdmin)