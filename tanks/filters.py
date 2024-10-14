from django.db.models import BooleanField
from django_filters import FilterSet, NumberFilter, BooleanFilter

from .models import Tank


class TankFilter(FilterSet):
    avg_gun_rating_min = NumberFilter(field_name='avg_rating_tank__avg_gun_rating', lookup_expr='gte')
    avg_gun_rating_max = NumberFilter(field_name='avg_rating_tank__avg_gun_rating', lookup_expr='lte')
    avg_mobility_rating_min = NumberFilter(field_name='avg_rating_tank__avg_mobility_rating', lookup_expr='gte')
    avg_mobility_rating_max = NumberFilter(field_name='avg_rating_tank__avg_mobility_rating', lookup_expr='lte')
    avg_detection_rating_min = NumberFilter(field_name='avg_rating_tank__avg_detection_rating', lookup_expr='gte')
    avg_detection_rating_max = NumberFilter(field_name='avg_rating_tank__avg_detection_rating', lookup_expr='lte')
    avg_armor_rating_min = NumberFilter(field_name='avg_rating_tank__avg_armor_rating', lookup_expr='gte')
    avg_armor_rating_max = NumberFilter(field_name='avg_rating_tank__avg_armor_rating', lookup_expr='lte')
    avg_cammo_rating_min = NumberFilter(field_name='avg_rating_tank__avg_cammo_rating', lookup_expr='gte')
    avg_cammo_rating_max = NumberFilter(field_name='avg_rating_tank__avg_cammo_rating', lookup_expr='lte')
    avg_overall_rating_min = NumberFilter(field_name='avg_rating_tank__avg_overall_rating', lookup_expr='gte')
    avg_overall_rating_max = NumberFilter(field_name='avg_rating_tank__avg_overall_rating', lookup_expr='lte')
    is_premium = BooleanFilter(field_name='is_premium')

    class Meta:
        model = Tank
        fields = [
            'type', 'tier', 'nation', 'is_premium', 'name',
            'avg_gun_rating_min', 'avg_gun_rating_max',
            'avg_mobility_rating_min', 'avg_mobility_rating_max',
            'avg_detection_rating_min', 'avg_detection_rating_max',
            'avg_armor_rating_min', 'avg_armor_rating_max',
            'avg_cammo_rating_min', 'avg_cammo_rating_max',
            'avg_overall_rating_min', 'avg_overall_rating_max',
        ]
