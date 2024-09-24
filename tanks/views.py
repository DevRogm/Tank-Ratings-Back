from rest_framework.generics import ListAPIView
from .models import Tank
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TankSerializer


# Create your views here.

class TankListApiView(ListAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nation', 'name', 'tier', 'type', 'is_premium']


#TODO: dodać tutaj pole z AvgRating i z listą komentarzy