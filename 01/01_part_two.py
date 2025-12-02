STARTING_POSITION = 50
DIAL_SIZE = 100

def determine_new_position(starting_position, line):
    dial_distance = int(line[1:])
    if line[0] == 'L':
        return (starting_position - dial_distance) % DIAL_SIZE
    return (starting_position + dial_distance) % DIAL_SIZE


def determine_amount_of_zeroes_passed(starting_position, line):
    dial_distance = int(line[1:])
    if line[0] == 'L':
        remainder = dial_distance % DIAL_SIZE
        return dial_distance // DIAL_SIZE + (starting_position != 0 and remainder >= starting_position)
    else:
        return (starting_position + dial_distance) // DIAL_SIZE


with open('./input') as input_file:
    current_position = STARTING_POSITION
    tally_zeroes = 0

    for current_line in input_file:
        initial_position = current_position
        amount_of_zeroes_passed = determine_amount_of_zeroes_passed(current_position, current_line)
        current_position = determine_new_position(current_position, current_line)
        tally_zeroes += amount_of_zeroes_passed

    print(tally_zeroes)