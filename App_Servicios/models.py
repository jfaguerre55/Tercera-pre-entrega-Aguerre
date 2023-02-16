from django.db import models

# Create your models here.

class Servicio(models.Model):

    name = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    fecha_alta = models.DateField()
    estado = models.BooleanField()

    def __str__(self) -> str:
        return self.name


class Cliente(models.Model):

    name = models.CharField(max_length=20)
    cuit = models.IntegerField()
    fecha_alta = models.DateField()
    domicilio = models.CharField(max_length=20)
    mail = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Activo(models.Model):

    name = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    fecha_alta = models.DateField()
    descripcion = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return self.name


class Empleado(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    legajo = models.IntegerField()
    fecha_nac = models.DateField()
    mail = models.EmailField()

    def __str__(self) -> str:
        return self.name