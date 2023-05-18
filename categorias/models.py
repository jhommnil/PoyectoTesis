from django.db import models

# Create your models here.
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