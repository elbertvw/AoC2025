# Definition of invalid: "Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times)
# are all invalid IDs."
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache

INPUT_FILENAME = 'input'

@lru_cache(None)
def find_divisors(n):
    divisors = []
    for number in range(1, n // 2 + 1):
        if n % number == 0:
            divisors.append(number)

    return divisors


def consists_of_equal_groups(identifier, group_size):
    group = identifier[:group_size]
    return identifier == group * (len(identifier) // group_size)


def is_valid(identifier):
    id_length = len(identifier)
    for divisor in find_divisors(id_length):
        if consists_of_equal_groups(identifier, divisor):
            return False
    return True


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