from geopy import distance


def get_distance(point_1, point_2):
    return distance.great_circle(point_1, point_2).miles
