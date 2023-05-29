from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.serializers import TruckSerializer
from trucks.models import Truck


class TruckViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
