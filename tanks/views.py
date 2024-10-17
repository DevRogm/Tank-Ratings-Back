from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .filters import TankFilter
from .models import Tank
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TankSerializer


# Create your views here.
class TankBaseApiView:
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    permission_classes = [AllowAny]

class TankListApiView(TankBaseApiView, ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TankFilter

class TankDetailsApiView(TankBaseApiView, RetrieveAPIView):
    pass

class TankTop10ApiView(TankBaseApiView, ListAPIView):
    queryset = Tank.objects.filter(avg_rating_tank__isnull=False).order_by('-avg_rating_tank__avg_overall_rating')[:10]

class TankAvailableApiView(TankBaseApiView, ListAPIView):
    permission_classes = [IsAuthenticated]
    #TODO: This should display a list of available tanks for the player to rate
    # This can be completed when WotClient is developed
    # A player can rate tanks if he has played more than 50 battles on them