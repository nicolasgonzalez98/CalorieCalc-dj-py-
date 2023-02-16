import django_filters
from .models import *

class foodItemFilter(django_filters.FilterSet):
    class Meta:
        model = ComidaItem
        fields = {
            'nombre':['contains']
        }