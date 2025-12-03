# Definition of invalid: "Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times)
# are all invalid IDs."
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache

INPUT_FILENAME = 'input'

@lru_cache(None)
def find_divisors(n):
    return [divisor for divisor in range(1, n // 2 + 1) if n % divisor == 0]


def consists_of_equal_groups(id, group_size):
    group = id[:group_size]
    return id == group * (len(id) // group_size)


def is_valid(id):
    id_length = len(id)
    for divisor in find_divisors(id_length):
        if consists_of_equal_groups(id, divisor):
            return False
    return True


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