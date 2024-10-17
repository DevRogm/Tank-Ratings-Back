from rest_framework import serializers

from accounts.serializers import UserSerializer
from ratings.models import Rating, Comment, AvgRating
from tanks.models import Tank
from tanks.serializers import TankSerializer, TankBaseSerializer
from django.db import models, transaction


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
        exclude = ('author', 'overall_rating')

    def validate(self, attrs):
        request = self.context.get('request')
        if Rating.objects.filter(tank=attrs.get('tank'), author=request.user).exists():
            raise serializers.ValidationError("Już oceniłeś ten czołg.")
        return attrs

    def create(self, validated_data):
        try:
            comment_data = validated_data.pop('comment', None)
            list_of_rating = [value for key, value in validated_data.items() if 'overall' not in key and 'rating' in key]
            overall_rating = sum(list_of_rating) / len(list_of_rating)
            rating = Rating.objects.create(**validated_data, overall_rating=overall_rating)
            rating.save()
            if comment_data:
                comment = Comment.objects.create(**comment_data)
                rating.comment = comment
                rating.save()
            return rating
        except Exception as e:
            print(str(e))
            raise serializers.ValidationError({"detail": "Wystąpił błąd podczas tworzenia oceny"})

    def update(self, instance, validated_data):
        try:
            with transaction.atomic():
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
                for attr, value in validated_data.items():
                    setattr(instance, attr, value)
                list_of_rating = [value for key, value in validated_data.items() if 'overall' not in key and 'rating' in key]
                overall_rating = sum(list_of_rating) / len(list_of_rating)
                instance.overall_rating = overall_rating
                instance.save()

                # Update avg_rating for the tank
                avg_rating = AvgRating.objects.filter(tank=instance.tank)
                if avg_rating:
                    tank = Tank.objects.get(id=instance.tank.id)
                    all_tank_ratings = tank.rating_tank.all()
                    rating_fields_name = [field.name for field in Rating._meta.get_fields() if "rating" in field.name]
                    avg_ratings = {f'avg_{rating}': all_tank_ratings.aggregate(models.Avg(rating))[f'{rating}__avg'] for rating in
                                   rating_fields_name}
                    avg_rating.update(**avg_ratings)
                return instance
        except Exception as e:
            print({str(e)})
            raise serializers.ValidationError({"detail": "Wystąpił błąd podczas aktualizacji oceny"})