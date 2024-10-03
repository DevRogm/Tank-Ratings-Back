from rest_framework import serializers
from ratings.models import Comment
from .models import Tank


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'created_at', 'updated_at')

class TankBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tank
        fields = ('name', 'nation', 'tier', 'type', 'is_premium', 'big_img', 'small_img')


class TankSerializer(TankBaseSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Tank
        fields = TankBaseSerializer.Meta.fields + ('comments', )

    @staticmethod
    def get_comments(obj):
        comments = Comment.objects.filter(rating_comment__tank=obj)
        return CommentSerializer(comments, many=True).data
