from rest_framework import generics
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import ActivateAccount

from .serializers import RegisterSerializer, ActivateAccountSerializer
from django.contrib.auth.models import User


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ActiveAccountCreateView(CreateAPIView):
    queryset = ActivateAccount.objects.all()
    serializer_class = ActivateAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class ActiveAccountRetrieveView(RetrieveAPIView):
    queryset = ActivateAccount.objects.all()
    serializer_class = ActivateAccountSerializer
    permission_classes = [IsAuthenticated]


class ActiveAccountDeleteView(DestroyAPIView):
    queryset = ActivateAccount.objects.all()
    permission_classes = [IsAuthenticated]
