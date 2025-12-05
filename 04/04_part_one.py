INPUT_FILENAME = 'input'
ROLL = '@'
EMPTY = '.'
MAX_ADJACENT_ROLLS = 4


def check_if_removable(lines, x, y):
    top, bottom = max(0, y - 1), min(len(lines), y + 2) # hacky way of taking into account the edges of the lines matrix
    left, right = max(0, x - 1), min(len(lines[y]), x + 2) # + 1 and + 2, because range() is x inclusive to y exclusive

    count = 0
    for yy in range(top, bottom):
        for xx in range(left, right):
            if lines[yy][xx] == ROLL: # the coord being checked is included, be aware that it too will be counted!
                count += 1
                if count > MAX_ADJACENT_ROLLS:
                    return False
    return True


def solve(input):
    lines = input.split('\n')
    result = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == ROLL:
                result += check_if_removable(lines, x, y)
    return result


with open(INPUT_FILENAME) as input_file:
    print(solve(input_file.read()))

# test case
# print(solve(TEST))  # = 13
