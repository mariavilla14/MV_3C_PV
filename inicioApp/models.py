from django.db import models

# Create your models here.
class aficionado(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono=models.CharField(max_length=12)
    fecha_nacimiento=models.DateField()
    codigo=models.IntegerField()


class usuario(models.Model):
    usuario=models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    direccion= models.CharField(max_length=45)
    fecha_registro = models.DateField()


class caricatura(models.Model):
    nombrec=models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    fecha_compra = models.DateField()
    codigov = models.IntegerField()