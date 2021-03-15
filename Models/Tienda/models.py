from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=50, null=False, unique=True)

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, null=False, unique=True)

class Producto(models.Model):
    marca = models.ForeignKey(Marca, null=False, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100, unique=True, null=False)
    descripcion_producto = models.TextField(null=True)
    precio = models.CharField(max_length=12, null=False)
    fecha_vencimiento = models.DateField(null=True)