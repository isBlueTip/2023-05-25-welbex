from django.contrib.gis.db import models as gis_models
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

from locations.constants import US_states_codes


class Location(TimeStampedModel, SoftDeletableModel):
    """
    Model Location:
    Attributes:
        - city: City name
        - state: State name
        - zip_code: Postal ZIP code
        - coordinates: Latitude and longitude of the location
    """

    city = models.CharField(db_index=True, null=False, blank=False, max_length=120, verbose_name="City")
    state = models.CharField(choices=US_states_codes, null=False, blank=False, verbose_name="State")
    zip_code = models.CharField(
        db_index=True, null=False, blank=False, max_length=5, verbose_name="ZIP code", unique=True
    )
    coordinates = gis_models.PointField(null=False, blank=False, verbose_name="Coordinates of the city")

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ("zip_code",)

    def __str__(self):
        return f"{self.city}, {self.state} ({self.zip_code})"
