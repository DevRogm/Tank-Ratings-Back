from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from .filters import RatingFilter
from .models import Rating
from .serializers import RatingListSerializer, RatingCreateSerializer


# Create your views here.
class RatingBase:
    queryset = Rating.objects.all()

class RatingListApiView(RatingBase, ListAPIView):
    serializer_class = RatingListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter

class RatingCreateApiView(RatingBase, CreateAPIView):
    serializer_class = RatingCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # TODO: dodać endpoint pod komentarze zeby wszystkie ogarnac
    # TODO: ogarnac permission, ogarnac filtrowanie
    # chciałbym widzieć listę komentarzy dla danego czołgu
    # średnie oceny dla czołgu
    # komentarze maja byc widoczne od najswiezszego do najstarszego w szczegółach czołgu
    # dodać create i retrieve dla ocen
    # później zmienic to na list ocen zalogowanego uzytkownika
    # ale w sumie list ocen przyda sie do wyswietlania ostatnich 10 ocen na stronie głównej
    # podczas dodawania ocen dla czołgu powinno byc utworzone AvgRating i wyliczane.
