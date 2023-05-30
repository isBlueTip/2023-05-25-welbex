from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

from locations.models import Location

MIN_CARGO_WEIGHT = 0
MAX_CARGO_WEIGHT = 1000


class Cargo(TimeStampedModel, SoftDeletableModel):
    """
    Model Cargo:
    Attributes:
        - pick_up_location: Pick-up cargo location
        - delivery_location: Delivery cargo location
        - weight: Weight of the cargo
        - description: Description of the cargo
    """

    pick_up_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, verbose_name="Cargo pick-up location", related_name="pick_up_cargos"
    )
    delivery_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, verbose_name="Cargo delivery location", related_name="delivery_cargos"
    )
    weight = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        verbose_name="Weight of the cargo",
        validators=[MinValueValidator(limit_value=MIN_CARGO_WEIGHT), MaxValueValidator(limit_value=MAX_CARGO_WEIGHT)],
    )
    description = models.TextField(max_length=200, verbose_name="Cargo description")

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargo"
        ordering = ("-id",)

    def __str__(self):
        return f"Cargo {self.pk}"
