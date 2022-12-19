from django.db import models

# Create your models here.


class Propietario(models.Model):
    TIPOS_DOCUMENTO = (('CC', 'Cédula Ciudadanía'),
                       ('CE', 'Cédula Extranjería'), ('NIT', 'NIT'))

    tipo_documento = models.CharField(
        max_length=3, choices=TIPOS_DOCUMENTO, default='CC')
    numero_documento = models.IntegerField(unique=True)
    nombres_apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50, null=True)
    numero_telefono = models.IntegerField(null=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombres_apellidos

    class Meta:
        unique_together = ('tipo_documento', 'numero_documento')


class Vehiculo(models.Model):
    placa = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=20, null=True)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField()
    color = models.CharField(max_length=15, blank=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    observaciones = models.TextField(max_length=255, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marca + " - " + self.placa
