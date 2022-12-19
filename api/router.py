from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('propietarios', views.PropietarioViewSet,
                basename='propietarios')
router.register('vehiculos', views.VehiculoViewSet, basename='vehiculos')

urlpatterns = [
    path('', include(router.urls)),
    path('propietarios/<int:propietario_documento>/vehiculos',
         views.VehiculodePropietarioView.as_view()),
    path('vehiculos/<str:placa_vehiculo>/propietario',
         views.PropietariodeVehiculoView.as_view()),
]
