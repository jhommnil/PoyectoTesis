from django.db import models
from categorias.models import MarcaImpresora, ModeloImpresora, TipoImpresora, ConectividadImpresora
from Stock.models import Impresoras
# Create your models here.

class Venta(models.Model):
    OPCIONES_PRODUCTO = (
        ('impresora', 'Impresora'),
        ('monitor', 'Monitor'),
        ('teclado', 'Teclado'),
        ('mause', 'Mause'),
    )

    producto = models.CharField(max_length=10, choices=OPCIONES_PRODUCTO)
    marca = models.ForeignKey(MarcaImpresora, on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.ForeignKey(ModeloImpresora, on_delete=models.CASCADE, null=True, blank=True)
    # Otros campos relevantes para la venta

    def save(self, *args, **kwargs):
        # Disminuir el stock automáticamente
        if self.producto == 'impresora':
            impresora = Impresoras.objects.get(marca=self.marca, modelo=self.modelo)
            impresora.cantidad -= 1
            impresora.save()
        super().save(*args, **kwargs)