from rest_framework import serializers
from ratings.models import Comment, AvgRating
from .models import Tank


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'created_at', 'updated_at')


class AvgRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvgRating
        fields = [
            'avg_gun_rating',
            'avg_mobility_rating',
            'avg_detection_rating',
            'avg_armor_rating',
            'avg_cammo_rating',
            'avg_overall_rating'
        ]


class TankBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('name', 'nation', 'tier', 'type', 'is_premium', 'big_img', 'small_img')


class TankSerializer(TankBaseSerializer):
    comments = serializers.SerializerMethodField()
    avg_ratings = AvgRatingSerializer(source='avg_rating_tank', read_only=True)

    class Meta:
        model = Tank
        fields = TankBaseSerializer.Meta.fields + ('comments', 'avg_ratings')

    is_premium = serializers.BooleanField()

    @staticmethod
    def get_comments(obj):
        comments = [rating.comment for rating in obj.rating_tank.all() if rating.comment is not None]
        return CommentSerializer(comments, many=True).data
