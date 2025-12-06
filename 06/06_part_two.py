from functools import reduce
from operator import mul

INPUT_FILENAME = 'input'
OPERATIONS = {
    '+': lambda x: sum(x),
    '*': lambda x: reduce(mul, x)
}

with open(INPUT_FILENAME) as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    width = max(len(line) for line in lines) 
    lines = [line.ljust(width) for line in lines]
    final_column = width - 1 
    
    solution = 0
    numbers = []
    operator = ''
    
    for column in range(width):
        column_content = ''.join(line[column] for line in lines[:-1] if line[column] != ' ')
        if column_content: 
            numbers.append(int(''.join([n for n in column_content])))
            
        if lines[-1][column] in OPERATIONS: 
            operator = lines[-1][column]
            
        if not column_content or column == final_column: 
            solution += OPERATIONS[operator](numbers)
            numbers = []
                
print(solution) 
