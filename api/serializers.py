from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from cargo.models import Cargo
from core.utils import get_distance
from locations.models import Location
from trucks.models import Truck


class CargoSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.CharField(required=False)
    delivery_location = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Cargo
        fields = [
            "id",
            "weight",
            "description",
            "pick_up_location",
            "delivery_location",
        ]

    def create(self, validated_data):
        validated_data["pick_up_location"] = Location.objects.get(zip_code=validated_data.pop("pick_up_location"))
        validated_data["delivery_location"] = Location.objects.get(zip_code=validated_data.pop("delivery_location"))

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["pick_up_location"] = Location.objects.get(zip_code=validated_data.pop("pick_up_location"))
        validated_data["delivery_location"] = Location.objects.get(zip_code=validated_data.pop("delivery_location"))

        return super().update(instance, validated_data)

    def validate_pick_up_location(self, value):
        if not Location.objects.filter(zip_code=value).exists():
            raise serializers.ValidationError("Pick-up zipcode is unknown")
        return value

    def validate_delivery_location(self, value):
        if not Location.objects.filter(zip_code=value).exists():
            raise serializers.ValidationError("Delivery zipcode is unknown")
        return value

    def validate(self, data):
        if not data.get("pick_up_location"):
            raise serializers.ValidationError("Pick-up location zipcode has to be provided")
        if not data.get("delivery_location"):
            raise serializers.ValidationError("Delivery location zipcode has to be provided")

        return super().validate(data)


class CargoListSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.CharField(read_only=True)
    delivery_location = serializers.CharField(read_only=True)
    closest_trucks_num = serializers.SerializerMethodField("get_closest_trucks_num")

    class Meta:
        model = Cargo
        fields = [
            "id",
            "weight",
            "description",
            "pick_up_location",
            "delivery_location",
            "closest_trucks_num",
        ]

    def get_closest_trucks_num(self, obj):  # TODO refactor as DB's function
        num = 0
        for truck in Truck.objects.all():
            distance_to_pick_up = get_distance(obj.delivery_location.coordinates, truck.current_location.coordinates)
            if distance_to_pick_up <= 450:
                num += 1
        return num


class TruckSerializer(serializers.ModelSerializer):
    current_location = serializers.CharField(required=False)
    payload_capacity = serializers.IntegerField(
        required=False, validators=[MaxValueValidator(limit_value=1000), MinValueValidator(limit_value=0)]
    )
    unique_number = serializers.CharField(read_only=True)

    class Meta:
        model = Truck
        fields = ["id", "unique_number", "current_location", "payload_capacity"]

    def create(self, validated_data):
        validated_data["current_location"] = Location.objects.get(zip_code=validated_data.pop("current_location"))

        return super().update(validated_data)

    def update(self, instance, validated_data):
        validated_data["current_location"] = Location.objects.get(zip_code=validated_data.pop("current_location"))

        return super().update(instance, validated_data)

    def validate_current_location(self, value):
        if not Location.objects.filter(zip_code=value).exists():
            raise serializers.ValidationError("Location zipcode is unknown")
        return value
