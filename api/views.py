from api.models import Propietario, Vehiculo
from .serializers import PropietarioSerializer, VehiculoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class PropietarioViewSet(ModelViewSet):
    serializer_class = PropietarioSerializer
    queryset = Propietario.objects.all()


class VehiculoViewSet(ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()


class VehiculodePropietarioView(APIView):

    def get(self, request, propietario_documento):

        propietario = Propietario.objects.filter(
            numero_documento=propietario_documento).first()
        vehiculos = Vehiculo.objects.filter(propietario=propietario)
        vehiculosResponse = VehiculoSerializer(vehiculos, many=True).data

        return Response({'message': 'success', 'vehiculos': vehiculosResponse})


class PropietariodeVehiculoView(APIView):

    def get(self, request, placa_vehiculo):

        vehiculo = Vehiculo.objects.filter(placa=placa_vehiculo).first()
        propietario = Propietario.objects.filter(id=vehiculo.propietario.id)
        propietarioResponse = PropietarioSerializer(
            propietario, many=True).data

        return Response({'message': 'success', 'propietarios': propietarioResponse})
