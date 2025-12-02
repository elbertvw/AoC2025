STARTING_POSITION = 50
DIAL_SIZE = 100

def determine_new_position(starting_position, line):
    dial_distance = int(line[1:])
    if line[0] == 'L':
        return (starting_position - dial_distance) % DIAL_SIZE
    return (starting_position + dial_distance) % DIAL_SIZE


with open('./input') as input_file:
    current_position = STARTING_POSITION
    tally_zeroes = 0

    for current_line in input_file:
        current_position = determine_new_position(current_position, current_line)
        if current_position == 0:
            tally_zeroes += 1

    print(tally_zeroes)