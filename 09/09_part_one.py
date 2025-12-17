from itertools import combinations

INPUT_FILENAME = 'input'


def area_of_rectangle(tile1, tile2):
    x_dist = abs(tile1[0] - tile2[0]) + 1
    y_dist = abs(tile1[1] - tile2[1]) + 1
    return x_dist * y_dist


with open(INPUT_FILENAME) as file:
    tiles = [tuple(map(int, line.split(","))) for line in file]
    largest_rectangle = max(area_of_rectangle(tile1, tile2) for tile1, tile2 in combinations(tiles, 2))
    print(largest_rectangle)
