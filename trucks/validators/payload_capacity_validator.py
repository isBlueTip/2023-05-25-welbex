from django.core.exceptions import ValidationError


def validate_payload_capacity(capacity: int) -> None:
    if capacity < 0:
        raise ValidationError("Truck payload capacity has to be greater than 0")
    if not 0 < capacity <= 1000:
        raise ValidationError("Truck payload capacity has to be between 1 and 1000")
