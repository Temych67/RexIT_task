import datetime

from django.db.models import F
from django_filters import rest_framework as filters


class ClientCategoryFilterSet(filters.FilterSet):
    category = filters.CharFilter(field_name='category')
    gender = filters.CharFilter(field_name='gender')
    birth_date = filters.DateFilter()
    age = filters.NumberFilter(method='age_filter')
    age_range = filters.CharFilter(method='age_range_filter')

    def age_filter(self, queryset, name, value):
        return queryset.annotate(
            ages=datetime.date.today().year - F('birth_date__year')
        ).filter(ages=value)

    def age_range_filter(self, queryset, name, value):
        age_from, age_to = value.split(',')
        return queryset.annotate(
            ages=datetime.date.today().year - F('birth_date__year')
        ).filter(ages__gte=age_from, ages__lte=age_to)
