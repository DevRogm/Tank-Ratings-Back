from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .models import Rating, Comment
from .serializers import RatingSerializer


# Create your views here.

class RatingListApiView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("gun_rating",)

    #TODO: dodać filtry zeby mozna było wybierać wieksze lub mniejsze od, dodać endpoint pod komentarze zeby wszystkie ogarnac
    #TODO: ogarnac permission, ogarnac filtrowanie,
    # chciałbym widzieć listę komentarzy dla danego czołgu
    # średnie oceny dla czołgu
    # komentarze maja byc widoczne od najswiezszego do najstarszego w szczegółach czołgu
    # dodać create i retrieve dla ocen
    # wyswietlać tekst komenatarzy a nie id.
