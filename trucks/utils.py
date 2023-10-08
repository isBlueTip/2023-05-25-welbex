from random import choice

from trucks.models import Truck
from cargo.models import Cargo
from core.utils import get_distance

from locations.models import Location

CLOSEST_TRUCK_CRITERION = 450


def get_random_location_id() -> int:
    locations_ids = Location.objects.values_list("id", flat=True)
    return choice(locations_ids)


def closest_trucks_num(cargo: Cargo) -> int:
    num = 0
    for truck in Truck.objects.all():
        distance_to_pick_up = get_distance(cargo.delivery_location.coordinates, truck.current_location.coordinates)
        if distance_to_pick_up <= CLOSEST_TRUCK_CRITERION:
            num += 1
    return num
