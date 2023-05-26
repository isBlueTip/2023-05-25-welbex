from django.db import models

from locations.models import Location


class Truck(models.Model):
    unique_number = models.CharField(max_length=5, unique=True, verbose_name="Truck number")
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    payload_capacity = models.PositiveIntegerField(verbose_name="Max cargo weight carried by the truck")

    def __str__(self):
        return self.unique_number
