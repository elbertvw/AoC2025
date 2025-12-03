# Definition of invalid: "You can find the invalid IDs by looking for any ID which is made only of some sequence of
# digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs."
from concurrent.futures import ProcessPoolExecutor

INPUT_FILENAME = 'input'

def is_valid(id):
    id_length = len(id)

    if id_length % 2 != 0:
        return True

    consists_of_equal_halves = id[:id_length // 2] == id[(id_length // 2):]
    return not consists_of_equal_halves


def sum_invalid_ids_in_range(range_string):
    lower_bound, upper_bound = map(int, range_string.split('-'))
    return sum(id for id in range(lower_bound, upper_bound + 1) if not is_valid(str(id)))


def main():
    with open(INPUT_FILENAME) as input_file:
        range_strings = input_file.read().split(',')

    with ProcessPoolExecutor() as executor:
        results = executor.map(sum_invalid_ids_in_range, range_strings)

    print(sum(results))

if __name__ == "__main__":
    main()