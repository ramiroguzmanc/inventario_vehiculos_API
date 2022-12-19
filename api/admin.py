from django.contrib import admin
from .models import Propietario, Vehiculo

# Register your models here.


@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ['nombres_apellidos']


@admin.register(Vehiculo)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ['placa', 'marca', 'propietario']
