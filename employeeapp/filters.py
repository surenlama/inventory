import django_filters
from .models import Store

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        fields = {
            'name': ['exact'],
            
        }