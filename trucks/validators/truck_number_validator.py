import re

from django.core.exceptions import ValidationError

from trucks.constants import TRUCK_UNIQUE_NUMBER_REGEX


def validate_unique_truck_number(number: str) -> None:
    if not re.match(TRUCK_UNIQUE_NUMBER_REGEX, number):
        raise ValidationError("Truck number has to be in format <4321A>")
