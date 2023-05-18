from django.db import models
from categorias.models import MarcaImpresora, ModeloImpresora, TipoImpresora, ConectividadImpresora
# Create your models here.

# Creamos el modelo impresora
class Impresoras(models.Model):
    marca=models.ForeignKey(MarcaImpresora, on_delete=models.CASCADE)
    modelo=models.ForeignKey(ModeloImpresora, on_delete=models.CASCADE)
    conectividad=models.ForeignKey(ConectividadImpresora, on_delete=models.CASCADE)
    precio_venta=models.DecimalField(max_digits=8, decimal_places=2)
    cantidad=models.IntegerField(default=0)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=10)



