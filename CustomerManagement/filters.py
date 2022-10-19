import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class ReceiptFilter(django_filters.FilterSet):
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Receipt
        fields = '__all__'
        exclude = ['citizen', 'date_created']
