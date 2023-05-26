from random import choice

from locations.models import Location


def get_random_location_id():
    locations_ids = Location.objects.values_list("id", flat=True)
    return choice(locations_ids)
