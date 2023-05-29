import random
import string

from django.db import models

from locations.models import Location
from trucks.validators import validate_payload_capacity, validate_unique_truck_number


class Truck(models.Model):
    unique_number = models.CharField(
        max_length=5, blank=True, unique=True, verbose_name="Truck number", validators=[validate_unique_truck_number]
    )
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="trucks")
    payload_capacity = models.PositiveIntegerField(
        verbose_name="Max cargo weight carried by the truck", validators=[validate_payload_capacity]
    )

    def __str__(self):
        return self.unique_number

    def save(self, *args, **kwargs):
        if not self.unique_number:
            self.unique_number = self.generate_unique_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_number():
        while True:
            number = random.randint(1000, 9999)
            letter = random.choice(string.ascii_uppercase)
            unique_number = f"{number}{letter}"

            if not Truck.objects.filter(unique_number=unique_number).exists():
                return unique_number
