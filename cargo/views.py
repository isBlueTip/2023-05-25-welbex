from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import CargoListSerializer, CargoSerializer
from cargo.filters import CargoFilter
from cargo.models import Cargo
from core.utils import get_distance
from trucks.models import Truck


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CargoFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CargoListSerializer
        return CargoSerializer

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = serializer.data

        data["trucks"] = {}

        for truck in Truck.objects.all():
            distance_to_pick_up = get_distance(
                instance.delivery_location.coordinates, truck.current_location.coordinates
            )
            data["trucks"][truck.unique_number] = distance_to_pick_up

        return Response(data)
