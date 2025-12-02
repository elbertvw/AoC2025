INPUT_FILENAME = 'input'
STARTING_POSITION = 50
DIAL_SIZE = 100

def determine_new_position(starting_position, line):
    dial_distance = int(line[1:])
    if line[0] == 'L':
        dial_distance = -dial_distance
    return (starting_position + dial_distance) % DIAL_SIZE


def determine_amount_of_zeroes_passed(starting_position, line):
    dial_distance = int(line[1:])
    if line[0] == 'L':
        full_dial_turns = dial_distance // DIAL_SIZE
        remainder = dial_distance % DIAL_SIZE
        optional_extra_turn = (starting_position != 0 and remainder >= starting_position)
        return full_dial_turns + optional_extra_turn
    else:
        return (starting_position + dial_distance) // DIAL_SIZE


with open(INPUT_FILENAME) as input_file:
    position = STARTING_POSITION
    total_zeroes = 0

    for line in input_file:
        zeroes_passed = determine_amount_of_zeroes_passed(position, line)
        position = determine_new_position(position, line)
        total_zeroes += zeroes_passed

    print(total_zeroes)