from rest_framework import serializers
from ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('author', 'tank', 'comment', 'gun_rating', 'mobility_rating', 'detection_rating', 'armor_rating', 'cammo_rating', 'overall_rating')
