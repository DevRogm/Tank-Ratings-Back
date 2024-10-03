from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Tank
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TankSerializer


# Create your views here.
class TankBaseApiView:
    queryset = Tank.objects.all()
    serializer_class = TankSerializer

class TankListApiView(TankBaseApiView, ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nation', 'name', 'tier', 'type', 'is_premium']

class TankDetailsApiView(TankBaseApiView, RetrieveAPIView):
    pass

#TODO: dodać tutaj pole z AvgRating i z listą komentarzy