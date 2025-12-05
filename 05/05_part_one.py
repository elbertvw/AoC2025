INPUT_FILENAME = 'input'


def id_in_range(id, range):
    return range[0] <= id <= range[1]


with open(INPUT_FILENAME) as input_file:
    lines = input_file.read().splitlines()
    id_ranges = [tuple(map(int, line.split('-'))) for line in lines if '-' in line]
    ingredient_ids = [int(line) for line in lines if '-' not in line and line.strip()]

    fresh_ingredients = set()
    for id in ingredient_ids:
        is_rotten = True
        for id_range in id_ranges:
            if id_in_range(id, id_range):
                is_rotten = False
                break
        if not is_rotten:
            fresh_ingredients.add(id)

print(len(fresh_ingredients))