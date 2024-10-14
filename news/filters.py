from django.db.models import CharField
from django_filters import FilterSet, CharFilter, DateTimeFilter
from .models import News


class NewsFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='exact')
    text = CharFilter(field_name='text', lookup_expr='icontains')
    created_at__gte = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = News
        fields = ['title', 'text', 'created_at']
