STARTING_POSITION = 50
DIAL_SIZE = 100

def determine_new_position(starting_position, line):
    dial_distance = int(line[1:])
    if line[0] == 'L':
        return (starting_position - dial_distance) % DIAL_SIZE
    return (starting_position + dial_distance) % DIAL_SIZE


with open('./input') as input_file:
    position = STARTING_POSITION
    total_zeroes = 0

    for line in input_file:
        position = determine_new_position(position, line)
        total_zeroes += (position == 0)

    print(total_zeroes)