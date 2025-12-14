from math import prod, dist
from itertools import combinations

CIRCUITS_TO_MULTIPLY = 3
CONNECTIONS_TO_MAKE = 1000
INPUT_FILENAME = 'input'


def calculate_distances(coordinates):
    return [((coord1, coord2), dist(coord1, coord2)) for coord1, coord2 in combinations(coordinates, 2)]


def find_circuits(pairs):
    circuits = []

    for (coord1, coord2) in pairs:
        new_circuit = {coord1, coord2}
        overlapping_circuits =  [circuit for circuit in circuits if circuit.intersection(new_circuit)]
        if overlapping_circuits:
            for circuit in overlapping_circuits:
                new_circuit = new_circuit.union(circuit)
                circuits.remove(circuit)
        circuits.append(new_circuit)

    return circuits


with open(INPUT_FILENAME) as file:
    coordinates = [tuple(map(int, line.split(","))) for line in file]

    pairs_with_distances = calculate_distances(coordinates)
    pairs_with_distances.sort(key=lambda x: x[1]) # sort by dist asc
    pairs_to_connect = [pair for pair, distance in pairs_with_distances[:CONNECTIONS_TO_MAKE]]

    circuits = find_circuits(pairs_to_connect)
    circuits.sort(key=len, reverse=True) # sort by len desc

    product = prod(len(c) for c in circuits[:CIRCUITS_TO_MULTIPLY])
    print(product)
