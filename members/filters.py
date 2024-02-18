from .models import Payment
from django_filters import rest_framework as filters

class PaymentFilter(filters.FilterSet):
    course = filters.CharFilter(field_name='course__title', lookup_expr='icontains')
    lesson = filters.CharFilter(field_name='lesson__title', lookup_expr='icontains')
    payment_method = filters.ChoiceFilter(field_name='payment_method', choices=[('cash', 'Наличные'), ('transfer', 'Перевод')])

    class Meta:
        model = Payment
        fields = []
