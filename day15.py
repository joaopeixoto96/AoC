import os
from functools import reduce
file_path = os.path.join('Advent of Code 2023','day15.txt')
input = [i for i in open(file_path).read().strip().split(',')]

# input = [30, 99, 109, 45]
# input = ['rn=1','cm-','qp=3','cm=2','qp-','pc=4','ot=9','ab=5','pc-','pc=6','ot=7']
# input = ['cm-']

result = 0
res_old = 0
out = []

def string_to_ascii(input_strings):
    ascii_codes_list = [[ord(character) for character in string] for string in input_strings]
    return ascii_codes_list

codes = string_to_ascii(input)
# print(codes)
results = []
for items in codes:
    for item in items:
        res_old = result + item
        res = ( res_old * 17 ) % 256
        result = res
    results.append(result)
    result = 0
print('Part 1 -',sum(results))


data = open(file_path).read().strip().split(',')

char = lambda i, c: (i+ord(c)) * 17 % 256
hash = lambda s: reduce(char, s, 0)

boxes = [dict() for _ in range(256)]

for step in data:
    match step.strip('-').split('='):
        case [l, f]: boxes[hash(l)][l] = int(f)
        case [l]:    boxes[hash(l)].pop(l, 0)

print('Part 2 -',sum(i*j*f for i,b in enumerate(boxes, 1)
                for j,f in enumerate(b.values(), 1)))