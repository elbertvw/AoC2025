import time

CIRCUITS_TO_MULTIPLY = 3
CONNECTIONS_TO_MAKE = 1000
INPUT_FILENAME = 'input'

TEST = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def find_distance(coordinate_1, coordinate_2):
    return sum((abs(a - b) ** 2) for a, b in zip(coordinate_1, coordinate_2)) ** 0.5


def calculate_distances(coordinates):
    result = []
    seen_coordinates = set()
    for current in coordinates:
        for other in coordinates:
            if current is not other and other not in seen_coordinates:
                result.append(((current, other), find_distance(current, other)))
        seen_coordinates.add(current)
    return result

def find_circuits(pairs_by_distances_asc):
    circuits = []
    for (coord1, coord2), _ in pairs_by_distances_asc[:CONNECTIONS_TO_MAKE]:
        new_circuit = {coord1, coord2}
        overlapping_circuits = []

        for circuit in circuits:
            if circuit & new_circuit: # check if intersection
                overlapping_circuits.append(circuit)

        if not overlapping_circuits:
            circuits.append(new_circuit) # add new
        else:
            for circuit in overlapping_circuits: # merge overlapping
                new_circuit |= circuit
                circuits.remove(circuit)
            circuits.append(new_circuit)

    return circuits


t0 = time.time()

with (open(INPUT_FILENAME) as file):
    coordinate_tuples = [(int(x), int(y), int(z)) for x, y, z in [line.strip().split(',') for line in file.readlines()]]
    # coordinate_tuples = [(int(x), int(y), int(z)) for x, y, z in [line.strip().split(',') for line in TEST.splitlines()]]
    coordinates_with_distances = calculate_distances(coordinate_tuples)
    coordinates_with_distances.sort(key=lambda x: x[1])

    # Find circuits
    circuits = find_circuits(coordinates_with_distances)
    circuits.sort(key=lambda x: len(x), reverse=True)
    for circuit in circuits:
        print(circuit)

    product = 1
    for circuit in circuits[:CIRCUITS_TO_MULTIPLY]:
        product *= len(circuit)
    print(product)

t1 = time.time()
print(f'Took {t1 - t0} seconds')





#
# def find_circuits(pairs_by_distances_asc):
#     result = []
#     for (coord1, coord2), distance in pairs_by_distances_asc[:CONNECTIONS_TO_MAKE]:
#         part_of_existing_circuit = False
#
#         for coord_set in result:
#             if coord1 in coord_set:
#                 coord_set.add(coord2)
#                 part_of_existing_circuit = True
#                 break
#
#             if coord2 in coord_set:
#                 coord_set.add(coord1)
#                 part_of_existing_circuit = True
#                 break
#
#         if not part_of_existing_circuit:
#             result.append({coord1, coord2})
#
#     # rudimentary merge of overlapping circuits due to limitations in addition to existing circuit
#     circuits_merged = 0
#     for i, coord_set in enumerate(result):
#         if result[i + 1].intersection(coord_set):
#             result[i] = coord_set.union(result.pop(i + 1))
#             circuits_merged += 1
#
#         if circuits_merged + i == len(result) - 1:
#             return result
#     return result

