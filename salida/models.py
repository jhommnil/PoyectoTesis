from django.db import models
from Stock.models import Impresoras
# Create your models here.


class VentaImpresora(models.Model):
    impresora = models.ForeignKey(Impresoras, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def save(self, *args, **kwargs):
        modelo_impresora = self.impresora.modelo
        if self.cantidad > self.impresora.cantidad:
            raise ValueError("No hay suficientes impresoras en stock")
        self.impresora.cantidad -= self.cantidad
        self.impresora.save()
        super().save(*args, **kwargs)
