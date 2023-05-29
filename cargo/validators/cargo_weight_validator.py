from django.core.exceptions import ValidationError


def validate_cargo_weight(weight: int) -> None:
    if weight < 0:
        raise ValidationError("Cargo weight has to be greater than 0")
    if not 0 < weight <= 1000:
        raise ValidationError("Cargo weight has to be between 1 and 1000")
