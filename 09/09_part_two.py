from itertools import combinations
from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])

INPUT_FILENAME = 'input'


# took me a while to find the proper term for this. TODO algo to be improved, I'm just happy it works for the time being
def orthogonal_polygonization(coordinates):
    result = []

    start_c = min(coordinates, key=lambda tile: tile.x)
    current_c = start_c
    next_c = None
    seen = {current_c}
    direction = 'up'

    while next_c != start_c:
        match direction:
            case "up":
                next_c = min(
                    (c for c in coordinates if c.x == current_c.x and c.y > current_c.y),
                    key=lambda c: c.y, default=None
                )
            case "right":
                next_c = min(
                    (c for c in coordinates if c.y == current_c.y and c.x > current_c.x),
                    key=lambda c: c.x, default=None
                )
            case "down":
                next_c = max(
                    (c for c in coordinates if c.x == current_c.x and c.y < current_c.y),
                    key=lambda c: c.y, default=None
                )
            case "left":
                next_c = max(
                    (c for c in coordinates if c.y == current_c.y and c.x < current_c.x),
                    key=lambda c: c.x, default=None
                )

        if next_c in coordinates and next_c not in seen:
            result.append((current_c, next_c))
            current_c = next_c
            seen.add(next_c)
            direction = 'up'
        else:
            direction = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}[direction]

    return result


def rectangle_does_not_intersect_outline(coordinate_tuple, outline):
    c1, c2 = coordinate_tuple
    left, right = min(c1.x, c2.x), max(c1.x, c2.x)
    bottom, top = min(c1.y, c2.y), max(c1.y, c2.y)

    for (x1, y1), (x2, y2) in outline:
        if y1 == y2: # horizontal line
            if bottom < y1 < top and max(x1, x2) > left and min(x1, x2) < right:
                return False
        elif x1 == x2: # vertical line
            if left < x1 < right and max(y1, y2) > bottom and min(y1, y2) < top:
                return False
    return True


def area_of_rectangle(c1, c2):
    return (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)


with open(INPUT_FILENAME) as file:
    coordinates = set(Coordinate(*map(int, line.split(","))) for line in file)
    outline = orthogonal_polygonization(coordinates)
    largest_rectangle = max(
        area_of_rectangle(c1, c2)
        for c1, c2 in combinations(coordinates, 2)
        if rectangle_does_not_intersect_outline((c1, c2), outline)
    )
    print(largest_rectangle)
