# Definition of invalid: "You can find the invalid IDs by looking for any ID which is made only of some sequence of
# digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs."
from concurrent.futures import ProcessPoolExecutor

INPUT_FILENAME = 'input'

def is_valid(identifier):
    id_length = len(identifier)

    if id_length % 2 != 0:
        return True

    consists_of_equal_halves = identifier[:id_length // 2] == identifier[(id_length // 2):]
    return not consists_of_equal_halves


def sum_invalid_identifiers_in_range(range_string):
    lower_bound, upper_bound = map(int, range_string.split('-'))
    sum_of_invalid_identifiers = 0
    for identifier in range(lower_bound, upper_bound + 1):
        if not is_valid(str(identifier)):
            sum_of_invalid_identifiers += identifier
    return sum_of_invalid_identifiers


def main():
    with open(INPUT_FILENAME) as input_file:
        range_strings = input_file.read().split(',')

    with ProcessPoolExecutor() as executor:
        results = executor.map(sum_invalid_identifiers_in_range, range_strings)

    print(sum(results))

if __name__ == "__main__":
    main()