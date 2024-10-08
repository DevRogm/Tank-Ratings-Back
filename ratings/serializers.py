from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from accounts.serializers import UserSerializer
from ratings.models import Rating, Comment
from tanks.models import Tank
from tanks.serializers import TankSerializer, TankBaseSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'created_at', 'updated_at')


class RatingListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tank = TankBaseSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'


class RatingCreateSerializer(serializers.ModelSerializer):
    tank = serializers.PrimaryKeyRelatedField(queryset=Tank.objects.all())
    comment = CommentSerializer(required=False)

    class Meta:
        model = Rating
        exclude = ('author',)

    def validate(self, attrs):
        request = self.context.get('request')

        if Rating.objects.filter(tank=attrs.get('tank'), author=request.user).exists():
            raise serializers.ValidationError("Już oceniłeś ten czołg.")
        return attrs

    def create(self, validated_data):
        comment_data = validated_data.pop('comment', None)
        rating = Rating.objects.create(**validated_data)
        if comment_data:
            comment = Comment.objects.create(**comment_data)
            rating.comment = comment
            rating.save()
        return rating

    def update(self, instance, validated_data):
        comment_data = validated_data.pop('comment', None)
        if comment_data:
            if instance.comment:
                comment_instance = instance.comment
                comment_instance.text = comment_data.get('text', comment_instance.text)
                comment_instance.save()
            else:
                comment = Comment.objects.create(**comment_data)
                instance.comment = comment
                instance.save()
        return instance