from rest_framework.generics import ListAPIView, RetrieveAPIView

from .filters import TankFilter
from .models import Tank
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TankSerializer


# Create your views here.
class TankBaseApiView:
    queryset = Tank.objects.all()
    serializer_class = TankSerializer

class TankListApiView(TankBaseApiView, ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TankFilter

class TankDetailsApiView(TankBaseApiView, RetrieveAPIView):
    pass
