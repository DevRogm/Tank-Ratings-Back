from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .filters import NewsFilter
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class NewsListApiView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
    permission_classes = [AllowAny]


class NewsDetailsApiView(RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [IsAuthenticated]


class NewsCreateApiView(CreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsDeleteApiView(DestroyAPIView):
    queryset = News.objects.all()
    permission_classes = [IsAdminUser]


class NewsUpdateApiView(UpdateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [IsAdminUser]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
