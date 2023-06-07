from django.db import models
from Stock.models import Impresoras, Monitor, Tplink,Teclado
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

class VentaMonitor(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def save(self, *args, **kwargs):
        modelo_Monitor = self.monitor.modelo
        if self.cantidad > self.monitor.cantidad:
            raise ValueError("No hay suficientes impresoras en stock")
        self.monitor.cantidad -= self.cantidad
        self.monitor.save()
        super().save(*args, **kwargs)

class VentaTplink(models.Model):
    tplink = models.ForeignKey(Tplink, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def save(self, *args, **kwargs):
        modelo_Tplink = self.tplink.modelo
        if self.cantidad > self.tplink.cantidad:
            raise ValueError("No hay suficientes impresoras en stock")
        self.tplink.cantidad -= self.cantidad
        self.tplink.save()
        super().save(*args, **kwargs)

class VentaTeclado(models.Model):
    teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def save(self, *args, **kwargs):
        modelo_Teclado = self.teclado.modelo
        if self.cantidad > self.teclado.cantidad:
            raise ValueError("No hay suficientes impresoras en stock")
        self.teclado.cantidad -= self.cantidad
        self.teclado.save()
        super().save(*args, **kwargs)