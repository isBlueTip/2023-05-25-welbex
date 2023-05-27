import django.db.models
from rest_framework import serializers

from cargo.models import Cargo
from locations.models import Location
from trucks.models import Truck


class TruckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        # fields = ['unique_number', 'distance_to_cargo']
        fields = [
            "unique_number",
        ]


class CargoSerializer(serializers.ModelSerializer):
    pick_up_zipcode = serializers.CharField(write_only=True)
    delivery_zipcode = serializers.CharField(write_only=True)
    pick_up_location = serializers.CharField(read_only=True)
    delivery_location = serializers.CharField(read_only=True)

    class Meta:
        model = Cargo
        fields = [
            "id",
            "pick_up_zipcode",
            "delivery_zipcode",
            "weight",
            "description",
            "pick_up_location",
            "delivery_location",
        ]

    def create(self, validated_data):
        validated_data["pick_up_location"] = validated_data.pop("pick_up_zipcode")
        validated_data["delivery_location"] = validated_data.pop("delivery_zipcode")

        return super().create(validated_data)

    def validate_weight(self, value):
        if not 0 < value <= 1000:
            raise serializers.ValidationError("Cargo weight has to be between 1 and 1000")
        return value

    def validate_pick_up_zipcode(self, value):
        try:
            return Location.objects.get(zip_code=value)
        except django.db.models.ObjectDoesNotExist:
            raise serializers.ValidationError("Pick-up zipcode is unknown")
        # return location

    def validate_delivery_zipcode(self, value):
        try:
            return Location.objects.get(zip_code=value)
        except django.db.models.ObjectDoesNotExist:
            raise serializers.ValidationError("Delivery zipcode is unknown")
        # return location


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ["unique_number", "current_location", "payload_capacity"]
