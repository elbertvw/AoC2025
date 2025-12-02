# Solution for 02 part two.

# Definition of invalid: "Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times)
# are all invalid IDs."

def find_divisors(identifier):
    divisors = []
    for number in range(1, identifier // 2 + 1):
        if identifier % number == 0:
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


with open('input') as input_file:
    range_strings = input_file.read().split(',')
    sum_of_invalid_identifiers = 0

    for range_string in range_strings:
        lower_bound, upper_bound = map(int, range_string.split('-'))
        for identifier in range(lower_bound, upper_bound + 1):
            if not is_valid(str(identifier)):
                sum_of_invalid_identifiers += identifier

    print(sum_of_invalid_identifiers)