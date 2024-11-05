from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from accounts.models import WotPlayer
from accounts.permissions import IsWotPlayer
from .filters import TankFilter
from .models import Tank
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TankSerializer


# Create your views here.
class TankBaseApiView:
    queryset = Tank.objects.select_related('avg_rating_tank').prefetch_related('rating_tank__comment').all()
    serializer_class = TankSerializer
    permission_classes = [AllowAny]


class TankListApiView(TankBaseApiView, ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TankFilter


class TankDetailsApiView(TankBaseApiView, RetrieveAPIView):
    pass


class TankTop10ApiView(TankBaseApiView, ListAPIView):
    queryset = Tank.objects.filter(avg_rating_tank__isnull=False).select_related('avg_rating_tank').prefetch_related(
        'rating_tank__comment').order_by('-avg_rating_tank__avg_overall_rating')[:10]


class TankAvailableApiView(TankBaseApiView, ListAPIView):
    permission_classes = [IsWotPlayer]

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            try:
                queryset = self.request.user.wot_player.available_tanks.select_related(
                    'avg_rating_tank').prefetch_related('rating_tank').all()
            except Exception:
                return queryset
        return queryset
