import csv
from django.db import migrations, models
from django.contrib.gis.geos import Point


def populate_locations(apps, schema_editor):
    Location = apps.get_model('locations', 'Location')

    with open('uszips.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            zip_code = row[0]
            latitude = row[1]
            longitude = row[2]
            city = row[3]
            state = row[4]

            location = Location.objects.update_or_create(
                city=city,
                state=state,
                zip_code=zip_code,
                coordinates=(Point(x=float(latitude), y=float(longitude))),
            )


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            populate_locations,
            migrations.RunPython.noop,
        )
    ]
