from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

from cargo.validators import validate_cargo_weight
from locations.models import Location


class Cargo(TimeStampedModel, SoftDeletableModel):
    pick_up_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, verbose_name="Cargo pick-up location", related_name="pick_up_cargos"
    )
    delivery_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, verbose_name="Cargo delivery location", related_name="delivery_cargos"
    )
    weight = models.PositiveIntegerField(verbose_name="Weight of the cargo", validators=[validate_cargo_weight])
    description = models.TextField(max_length=200, verbose_name="Cargo description")

    def __str__(self):
        return f"Cargo {self.pk}"
