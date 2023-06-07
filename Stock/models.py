from django.db import models
from categorias.models import MarcaImpresora, ModeloImpresora, TipoImpresora, ConectividadImpresora
from categorias.models import MarcaMonitor, ModeloMonitor, TipoMonitor, ConectividadMonitor
from categorias.models import MarcaTplink, ModeloTplink,TipoTplink,ConectividadTpelink
from categorias.models import MarcaTeclado,ModeloTeclado,TipoTeclado

# Create your models here.

# Creamos el modelo impresora
class Impresoras(models.Model):
    marca=models.ForeignKey(MarcaImpresora, on_delete=models.CASCADE)
    modelo=models.ForeignKey(ModeloImpresora, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoImpresora, on_delete=models.CASCADE)
    conectividad=models.ForeignKey(ConectividadImpresora, on_delete=models.CASCADE)
    precio_venta=models.DecimalField(max_digits=8, decimal_places=2)
    cantidad=models.IntegerField(default=0)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Monitor(models.Model):
    marca = models.ForeignKey(MarcaMonitor, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloMonitor, on_delete=models.CASCADE)
    tipo_pantalla=models.ForeignKey(TipoMonitor,on_delete=models.CASCADE,default=1)
    conectividad = models.ForeignKey(ConectividadMonitor, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca}{self.modelo}"

class Tplink(models.Model):
    marca = models.ForeignKey(MarcaTplink, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloTplink, on_delete=models.CASCADE)
    tipo= models.ForeignKey(TipoTplink,on_delete=models.CASCADE)
    conectividad = models.ForeignKey(ConectividadTpelink,on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca}{self.modelo}"

class Teclado(models.Model):
    marca = models.ForeignKey(MarcaTeclado, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloTeclado, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoTeclado,on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca}{self.modelo}"