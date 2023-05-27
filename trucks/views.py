from rest_framework import generics, mixins, views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers import TruckSerializer
from trucks.models import Truck


class TruckViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     data = serializer.data
    #     print(data)
    #     return super().update(request, *args, **kwargs)
