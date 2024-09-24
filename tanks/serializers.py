from rest_framework import serializers
from .models import Tank

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('name', 'nation', 'tier', 'type', 'is_premium', 'big_img', 'small_img')