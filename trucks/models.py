import random
import string

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from locations.models import Location
from trucks.constants import TRUCK_UNIQUE_NUMBER_REGEX

MIN_PAYLOAD_CAPACITY = 0
MAX_PAYLOAD_CAPACITY = 1000


class Truck(models.Model):
    """
    Model Truck:
    Attributes:
        - unique_number: Unique truck number
        - current_location: Current truck location
        - load_capacity: Max weight carried by the truck
    """

    unique_number = models.CharField(
        db_index=True,
        max_length=5,
        blank=True,
        unique=True,
        verbose_name="Truck number",
        validators=[
            RegexValidator(regex=TRUCK_UNIQUE_NUMBER_REGEX, message="Truck number has to be in format <4321A>")
        ],
    )
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="trucks")
    payload_capacity = models.PositiveSmallIntegerField(
        verbose_name="Max cargo weight carried by the truck",
        validators=[
            MinValueValidator(limit_value=MIN_PAYLOAD_CAPACITY),
            MaxValueValidator(limit_value=MAX_PAYLOAD_CAPACITY),
        ],
    )

    class Meta:
        verbose_name = "Truck"
        verbose_name_plural = "Trucks"
        ordering = ("unique_number",)

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
