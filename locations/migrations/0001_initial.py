# Generated by Django 4.2.1 on 2023-05-26 07:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                ("city", models.CharField(db_index=True, max_length=120, verbose_name="City")),
                ("state", models.CharField(max_length=120, verbose_name="State")),
                ("zip_code", models.CharField(max_length=5, unique=True, verbose_name="ZIP code")),
                (
                    "coordinates",
                    django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name="Coordinates of the city"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
