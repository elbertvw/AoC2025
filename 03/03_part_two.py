INPUT_FILENAME = 'input'
DIGITS_TO_SELECT = 12

def get_max_joltage(line):
    result = []
    left_bound = 0
    right_bound = len(line) - DIGITS_TO_SELECT

    while len(result) < DIGITS_TO_SELECT:
        range_to_check = line[left_bound:right_bound + 1]
        max_in_range = max(range_to_check)
        result.append(max_in_range)

        left_bound_moves = left_bound + range_to_check.index(max_in_range)
        left_bound = left_bound_moves + 1
        right_bound += 1

    return int(''.join(result))


with open(INPUT_FILENAME) as input_file:
    results = [get_max_joltage(line.strip()) for line in input_file]

print(sum(results))





