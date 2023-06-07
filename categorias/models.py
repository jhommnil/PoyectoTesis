from django.db import models

# Create your models here.
#clases para la tabla impresora
class MarcaImpresora(models.Model):
    marca = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marca

class ModeloImpresora(models.Model):
    modelo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.modelo

class TipoImpresora(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class ConectividadImpresora(models.Model):
    conectividad = models.CharField(max_length=100)

    def __str__(self):
        return self.conectividad

#clases para la tabla Monitores

class MarcaMonitor(models.Model):
    marca = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marca

class ModeloMonitor(models.Model):
    modelo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self. modelo

class TipoMonitor(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class ConectividadMonitor(models.Model):
    conectividad= models.CharField(max_length=100)

    def __str__(self):
        return self.conectividad

#Clases para la tablas tp-link

class MarcaTplink(models.Model):
    marca=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marca

class ModeloTplink(models.Model):
    modelo=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.modelo

class TipoTplink(models.Model):
    tipo=models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class ConectividadTpelink(models.Model):
    conectividad = models.CharField(max_length=100)

    def __str__(self):
        return self.conectividad

#calses para la tabla Teclados
class MarcaTeclado(models.Model):
    marca=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.marca
