from functools import lru_cache

INPUT_FILENAME = 'input'
START_CHAR = 'S'
SPLIT_CHAR = '^'

@lru_cache(None)
def sum_possible_paths(x, y, lines):
    if y == len(lines):
        return 1
    elif lines[y][x] == SPLIT_CHAR:
        return sum_possible_paths(x + 1, y + 1, lines) + sum_possible_paths(x - 1, y + 1, lines)
    else:
        return sum_possible_paths(x, y + 1, lines)

with open(INPUT_FILENAME) as file:
    lines = file.readlines()        
    start_x = lines[0].index(START_CHAR)
    print(sum_possible_paths(start_x, 0, tuple(lines))) # tuple is hashable for lru_cache purposes  
