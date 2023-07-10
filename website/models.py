from django.db import models

# Create your models here.

class Product(models.Model):
    tipoprod = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    imagen= models.ImageField(blank=True, null= True)
    precio = models.IntegerField()
    arrendado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

class Rents(models.Model):
    name = models.CharField(max_length=100)
    bicicleta = models.CharField(max_length=100)
    pago = models.IntegerField()
    fecha_ini = models.DateField()
    fecha_ter = models.DateField()

    def __str__(self):
        return self.nombre