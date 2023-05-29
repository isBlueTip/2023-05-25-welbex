import string
from random import choice, randint

from django.db import migrations, models


def populate_cargo(apps, schema_editor):
    Cargo = apps.get_model('cargo', 'Cargo')
    Location = apps.get_model('locations', 'Location')

    locations = Location.objects.all()
    num_of_locations = locations.count() - 1

    for i in range(0, 10):
        cargo = Cargo.objects.create(
            pick_up_location=Location.objects.all()[randint(1, num_of_locations)],
            delivery_location=Location.objects.all()[randint(1, num_of_locations)],
            weight=randint(1, 1000),
            description=f'Description of cargo #{i-1}'
        )


class Migration(migrations.Migration):
    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            populate_cargo,
            migrations.RunPython.noop,
        )
    ]
