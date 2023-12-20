import os
file_path = os.path.join('AoC_2023','day13.txt')

def reflection(rows, elements):
    for i in range(1, len(rows)):
        differences = 0
        for row1, row2 in zip(rows[i-1::-1], rows[i:]):
            for col1, col2 in zip(row1, row2):
                if col1 != col2:
                    differences += 1
        if differences == elements:
            return i
    else:
        return 0
input = list(map(str.splitlines, open(file_path).read().split('\n\n')))

    
for s in 0, 1:
    result = 0
    for row in input:
        reflection_sum = 100 * reflection(row,s) + reflection([*zip(*row)],s)
        result += reflection_sum
    print(f'Part {s+1} - {result}')