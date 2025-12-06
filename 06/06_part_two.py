from functools import reduce
from operator import mul

INPUT_FILENAME = 'input'

def calculate(numbers, operator):
    return sum(numbers) if operator == '+' else reduce(mul, numbers)


# Join characters in each column, strip spaces, remove empty columns
def clean_columns(columns):
    return [''.join(col).replace(' ', '') for col in columns if ''.join(col).strip()]


# If we reverse the input, we can use the operator as a delimiter separating problems 
with open(INPUT_FILENAME) as input_file:
    lines = [line[::-1] for line in input_file]
    height = len(lines)
    width = max(len(line) for line in lines)
    
    problems = []
    problem_columns = [[] for _ in range(height)]
    problem_column = 0 

    for column in range(width):
        end_of_current_problem = False

        for line in lines:
            char = line[column]
            if char in '+*': end_of_current_problem = True
            else: problem_columns[problem_column].append(char)

        if end_of_current_problem:
            numbers = [int(n) for n in clean_columns(problem_columns)]
            problems.append((numbers, char))
            problem_columns = [[] for _ in range(height)]
            problem_column = 0
        else:
            problem_column += 1

print(sum(calculate(numbers, op) for numbers, op in problems))