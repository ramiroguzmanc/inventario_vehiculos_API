from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Propietario, Vehiculo


class PropietarioSerializer(ModelSerializer):

    class Meta:
        model = Propietario
        fields = '__all__'


class VehiculoSerializer(ModelSerializer):

    # propietario_id = StringRelatedField()

    class Meta:
        model = Vehiculo
        fields = '__all__'
