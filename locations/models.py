from django.contrib.gis.db import models as gis_models
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class Location(TimeStampedModel, SoftDeletableModel):
    city = models.CharField(db_index=True, max_length=120, verbose_name="City")
    state = models.CharField(max_length=120, verbose_name="State")
    zip_code = models.CharField(max_length=5, verbose_name="ZIP code", unique=True)
    coordinates = gis_models.PointField(verbose_name="Coordinates of the city")

    def __str__(self):
        return f"{self.city}, {self.state} ({self.zip_code})"
