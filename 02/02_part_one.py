# Solution for 02 part one. An optimization could be to exclude entire ranges where the whole range consists of odd
# numbers, but I did not implement this (seemed overkill).

# Definition of invalid: "You can find the invalid IDs by looking for any ID which is made only of some sequence of
# digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs."

def is_valid(identifier):
    id_length = len(identifier)

    if id_length % 2 != 0:
        return True

    consists_of_equal_halves = identifier[:id_length // 2] == identifier[(id_length // 2):]
    return not consists_of_equal_halves


with open('input') as input_file:
    raw_ranges = input_file.read().split(',')
    range_tuples = [(id_range.split('-')[0], id_range.split('-')[1]) for id_range in raw_ranges]
    invalid_ids = []

    for range_tuple in range_tuples:
        for identifier in range(int(range_tuple[0]), int(range_tuple[1]) + 1):
            if not is_valid(str(identifier)):
                invalid_ids.append(identifier)

    print(sum(invalid_ids))