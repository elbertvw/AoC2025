from math import dist
from itertools import combinations

CIRCUITS_TO_MULTIPLY = 3
INPUT_FILENAME = 'input'


def calculate_distances(coordinates):
    return [((coord1, coord2), dist(coord1, coord2)) for coord1, coord2 in combinations(coordinates, 2)]


def find_last_connecting_pair(pairs):
    circuits = []
    last_connecting_pair = None

    for (coord1, coord2) in pairs:
        new_circuit = {coord1, coord2}

        # Very ugly solution, to be refactored -- finds multiple candidates and overwrites until the final one is found
        if len(circuits) == 1:
            if (coord1 in circuits[0] and coord2 not in circuits[0]) or (coord2 in circuits[0] and coord1 not in circuits[0]):
                last_connecting_pair = (coord1, coord2)

        overlapping_circuits =  [circuit for circuit in circuits if circuit.intersection(new_circuit)]
        if overlapping_circuits:
            for circuit in overlapping_circuits:
                new_circuit = new_circuit.union(circuit)
                circuits.remove(circuit)
        circuits.append(new_circuit)

    return last_connecting_pair


with open(INPUT_FILENAME) as file:
    coordinates = [tuple(map(int, line.split(","))) for line in file]
    pairs_with_distances = calculate_distances(coordinates)
    pairs_with_distances.sort(key=lambda x: x[1]) # sort by dist asc

    pairs_to_connect = [pair for pair, distance in pairs_with_distances]
    last_connecting_pair = find_last_connecting_pair(pairs_to_connect)
    solution = last_connecting_pair[0][0] * last_connecting_pair[1][0]
    print(solution)

