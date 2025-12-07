from math import prod

INPUT_FILENAME = 'input'
OPERATIONS = {
    '+': lambda x: sum(x),
    '*': lambda x: prod(x)
}

with open(INPUT_FILENAME) as file:
    lines = [line.strip()[::-1] for line in file.readlines()] # reversing facilitates using the operator as delimiter :)
    width = max(len(line) for line in lines) 
    lines = [line.rjust(width) for line in lines]
    
    solution = 0
    numbers = []
    
    for column in range(width):
        column_content = ''.join(line[column] for line in lines[:-1] if line[column] != ' ')
        if column_content: numbers.append(int(column_content))
        
        operator = lines[-1][column]
        if operator in OPERATIONS: 
            solution += OPERATIONS[operator](numbers)
            numbers = []
                
print(solution) 

