INPUT_FILENAME = 'input'


def merge_ranges(ranges):
    merged_ranges = [ranges[0]]

    for current_range in ranges:
        previous_range = merged_ranges[-1]
        if previous_range[1] >= current_range[0]:
            merged_ranges[-1] = (previous_range[0], max(previous_range[1], current_range[1]))
        else:
            merged_ranges.append(current_range)

    return merged_ranges


with open(INPUT_FILENAME) as input_file:
    ranges_asc = sorted(
        (tuple(map(int, line.split('-'))) for line in input_file if '-' in line),
        key=lambda x: x[0] # sort ranges by lower bound
    )

    merged = merge_ranges(ranges_asc)
    total = 0
    for r in merged:
        total += r[1] - r[0] + 1

    print(total)

