from django_filters import FilterSet, NumberFilter
from .models import Rating


class RatingFilter(FilterSet):
    gun_rating__gte = NumberFilter(field_name='gun_rating', lookup_expr='gte')
    gun_rating__lte = NumberFilter(field_name='gun_rating', lookup_expr='lte')
    mobility_rating__gte = NumberFilter(field_name='mobility_rating', lookup_expr='gte')
    mobility_rating__lte = NumberFilter(field_name='mobility_rating', lookup_expr='lte')
    detection_rating__gte = NumberFilter(field_name='detection_rating', lookup_expr='gte')
    detection_rating__lte = NumberFilter(field_name='detection_rating', lookup_expr='lte')
    armor_rating__gte = NumberFilter(field_name='armor_rating', lookup_expr='gte')
    armor_rating__lte = NumberFilter(field_name='armor_rating', lookup_expr='lte')
    cammo_rating__gte = NumberFilter(field_name='armor_rating', lookup_expr='lte')
    cammo_rating__lte = NumberFilter(field_name='armor_rating', lookup_expr='lte')
    overall_rating__gte = NumberFilter(field_name='armor_rating', lookup_expr='lte')
    overall_rating__lte = NumberFilter(field_name='armor_rating', lookup_expr='lte')

    class Meta:
        model = Rating
        fields = [
            'gun_rating',
            'mobility_rating',
            'detection_rating',
            'armor_rating',
            'cammo_rating',
            'overall_rating'
        ]

