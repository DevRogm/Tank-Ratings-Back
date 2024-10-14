from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = ['author', 'title', 'text', 'created_at', 'updated_at']
