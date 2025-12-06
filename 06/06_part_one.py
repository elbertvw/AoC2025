from functools import reduce
from operator import mul

INPUT_FILENAME = 'input'


def calculate(column):
    numbers = [int(n) for n in column[:-1]]
    return sum(numbers) if column[-1] == '+' else reduce(mul, numbers)


with open(INPUT_FILENAME) as input_file:
    split_lines = [line.split() for line in input_file.read().splitlines()]

    columns = [[] for _ in range(len(split_lines[0]))]
    for line in split_lines:
        for index, value in enumerate(line):
            columns[index].append(value)

    print(sum(calculate(column) for column in columns))