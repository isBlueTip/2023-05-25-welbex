from django_filters import rest_framework as filters

from cargo.models import Cargo


class CargoFilter(filters.FilterSet):
    weight = filters.NumberFilter()
    weight__gt = filters.NumberFilter(field_name="weight", lookup_expr="gt")
    weight__lt = filters.NumberFilter(field_name="weight", lookup_expr="lt")

    class Meta:
        model = Cargo
        fields = ["weight"]
