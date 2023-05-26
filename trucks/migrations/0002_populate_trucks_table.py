import string
from random import choice, randint

import django.db.utils
from django.db import migrations, models

from trucks.utils import get_random_location_id


def generate_unique_number():
    number = randint(1000, 9999)
    letter = choice(string.ascii_uppercase)
    unique_number = f"{number}{letter}"

    return unique_number


def populate_trucks(apps, schema_editor):
    Truck = apps.get_model('trucks', 'Truck')
    cnt = 0

    while 1:
        unique_number = generate_unique_number()
        try:
            truck = Truck.objects.create(
                unique_number=unique_number,
                current_location_id=get_random_location_id(),
                payload_capacity=randint(1, 1000),
            )
        except django.db.utils.IntegrityError:
            pass
        else:
            cnt += 1
        if cnt == 30:
            break


class Migration(migrations.Migration):
    dependencies = [
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            populate_trucks,
            migrations.RunPython.noop,
        )
    ]
