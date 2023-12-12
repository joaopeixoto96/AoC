import os
from functools import cache
file_path = os.path.join('Advent of Code 2023','day12.txt')
rows = open(file_path).read().splitlines()

@cache
def fit_count(pattern, counts):
    if len(counts) == 0:
        return '#' not in pattern

    biggest = max(counts)
    biggest_i = counts.index(biggest)
    left_counts, right_counts = counts[:biggest_i], counts[biggest_i+1:]

    start_buffer = sum(left_counts)+len(left_counts)
    end_buffer = sum(right_counts)+len(right_counts)

    total = 0
    for i in range(start_buffer, len(pattern)-end_buffer-biggest+1):
        block_pattern = pattern[i:i+biggest]
        left_border = "" if i == 0 else pattern[i-1]
        right_border = "" if i+biggest == len(pattern) else pattern[i+biggest]

        if '.' not in block_pattern and left_border != '#' and right_border != '#':
            left_total = fit_count(pattern[:i-len(left_border)], left_counts)
            right_total = fit_count(pattern[i+biggest+len(right_border):], right_counts)
            total += left_total * right_total
    return total

data = []
for line in rows:
    pattern, counts = line.split()
    data.append((pattern, tuple(int(x) for x in counts.split(','))))

print('Part 1 - ', sum(fit_count(*line) for line in data))

unfolded = [("?".join([pattern,]*5), counts*5) for pattern, counts in data]
print("Part 2:", sum(fit_count(*line) for line in unfolded))