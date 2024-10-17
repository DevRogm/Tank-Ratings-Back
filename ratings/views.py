from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.db import models, transaction

from accounts.permissions import IsOwnerOrReadOnly
from tanks.models import Tank
from .filters import RatingFilter
from .models import Rating, Comment, AvgRating
from .serializers import RatingListSerializer, RatingCreateSerializer


# Create your views here.
class RatingBase:
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]


class RatingListApiView(RatingBase, ListAPIView):
    serializer_class = RatingListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter
    permission_classes = [IsAdminUser]


class RatingCreateApiView(RatingBase, CreateAPIView):
    serializer_class = RatingCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)

                # create or update avg rating for the tank
                tank = Tank.objects.get(id=self.request.data["tank"])
                all_tank_ratings = tank.rating_tank.all()
                rating_fields_name = [field.name for field in Rating._meta.get_fields() if "rating" in field.name]
                avg_ratings = {f'avg_{rating}' : all_tank_ratings.aggregate(models.Avg(rating))[f'{rating}__avg'] for rating in rating_fields_name}
                AvgRating.objects.update_or_create(tank=tank, defaults=avg_ratings)
        except Exception as e:
            return Response({"error": "Wystąpił błąd podczas tworzenia oceny"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RatingUpdateApiView(RatingBase, UpdateAPIView):
    serializer_class = RatingCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class RatingDeleteApiView(RatingBase, DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, *args, **kwargs):
        rating = self.get_object()
        self.perform_destroy(rating)
        if rating.comment:
            rating.comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RatingDetailsApiView(RatingBase, RetrieveAPIView):
    serializer_class = RatingListSerializer


class CommentDeleteApiView(DestroyAPIView):
    queryset = Comment.objects.all()
