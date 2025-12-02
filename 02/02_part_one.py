# Solution for 02 part one.

# Definition of invalid: "You can find the invalid IDs by looking for any ID which is made only of some sequence of
# digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs."

def is_valid(identifier):
    id_length = len(identifier)

    if id_length % 2 != 0:
        return True

    consists_of_equal_halves = identifier[:id_length // 2] == identifier[(id_length // 2):]
    return not consists_of_equal_halves


with open('input') as input_file:
    range_strings = input_file.read().split(',')
    sum_of_invalid_identifiers = 0

    for range_string in range_strings:
        lower_bound, upper_bound = map(int, range_string.split('-'))
        for identifier in range(lower_bound, upper_bound + 1):
            if not is_valid(str(identifier)):
                sum_of_invalid_identifiers += identifier

    print(sum_of_invalid_identifiers)