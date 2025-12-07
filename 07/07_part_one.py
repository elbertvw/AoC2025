INPUT_FILENAME = 'input'
START_CHAR = 'S'
SPLIT_CHAR = '^'

with open(INPUT_FILENAME) as file:
    lines = file.readlines()
    beam_indices = {lines[0].index(START_CHAR)}
    splits = 0
    
    for line in lines[1:]: 
        split_indices = [index for index, char in enumerate(line) if char == SPLIT_CHAR]
        for split_index in split_indices:
            if split_index in beam_indices:
                beam_indices.update([split_index - 1, split_index + 1])
                beam_indices.remove(split_index)
                splits += 1
                
    print(splits)
        
    
    
