INPUT_FILENAME = 'input'

def merge_ascending_ranges(ranges):
    merged_ranges = [ranges[0]]

    for current_start, current_end in ranges:
        previous_start, previous_end = merged_ranges[-1]
        if previous_end >= current_start:
            merged_ranges[-1] = (previous_start, max(previous_end, current_end))
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges


with open(INPUT_FILENAME) as input_file:
    ranges_asc = sorted(
        (tuple(map(int, line.split('-'))) for line in input_file if '-' in line),
        key=lambda x: x[0] # sort ranges by lower bound
    )

    merged = merge_ascending_ranges(ranges_asc)
    total = 0
    for r in merged:
        total += r[1] - r[0] + 1

    print(total)

