INPUT_FILENAME = 'input'

def get_max_joltage(line):
    digits = [int(digit) for digit in line.strip()]
    highest_digit = max(digits)
    highest_index = digits.index(highest_digit)

    if highest_index == len(digits) - 1:
        second_highest_digit = max(digits[:highest_index])
        return int(f'{second_highest_digit}{highest_digit}')
    else:
        second_highest_digit = max(digits[highest_index + 1:])
        return int(f'{highest_digit}{second_highest_digit}')


with open(INPUT_FILENAME) as input_file:
    results = [get_max_joltage(line) for line in input_file]

print(sum(results))



