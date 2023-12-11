import os
import ast
import re
from math import gcd
file_path = os.path.join('Advent of Code 2023','day8.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()

commands = lines[0].strip()
commands_conv = commands.replace('L','0').replace('R','1')
network = lines[2:]

network_dict = {}
for line in network:
    parts = line.split('=')
    key = parts[0].strip()
    values = parts[1].strip()
    tuple_values = tuple(map(str.strip, values[1:-1].split(',')))
    network_dict[key] = values

'''Part 1'''
selected_key = 'AAA'
count = 0

while True:
    for item in commands_conv:
        value = tuple(map(str.split, network_dict[selected_key][1:-1].split(',')))
        if selected_key != 'ZZZ':
            selected_key_list = value[int(item)]
            new_key = selected_key_list[0]
            count += 1
        selected_key = new_key
        if selected_key == 'ZZZ':
            break
    else:
        commands_conv += commands_conv
        continue
    break
print(f'Part 1 - {count}')


#Never got it to work
# '''Part 2'''
# selected_keys= [key for key in network_dict.keys() if key[-1]=='A']
# # success_key = [key for key in selected_keys if key[-1] == 'Z']
# count = 0
# new_selected_keys = []
# while True:
#     for sel in selected_keys:
#         for item in commands_conv:
#             value = tuple(map(str.split, network_dict[sel][1:-1].split(',')))
#         new_selected_key = value[0]
#         new_selected_keys.append(new_selected_key[0])
#     result = [check.endswith('Z') for check in new_selected_keys]
#     if result == [False,False]:
#         selected_keys = new_selected_keys
#         count +=1
#     else:
#         break
    
    
# print(count)
#Use this instead
def parse(filename):
    s = open(filename).read().strip()
    cmd, body = s.split('\n\n')
    dic = {}
    for b in body.split('\n'):
        x,y,z = re.findall('\w+', b)
        dic[x] = [y, z]
    return cmd, dic

def runner(cmd, dic, start):
    i, stack = 0, [start]
    while 1:
        head = stack.pop()
        stack.append(dic[head][0] if cmd[i]=='L' else dic[head][1])
        i = (i+1) % len(cmd)
        yield head

def part2(cmd, dic):
    As = [key for key in dic.keys() if key[-1]=='A']
    gens = [runner(cmd, dic, A) for A in As]
    answer = 1
    for g in gens:
        rounds = 0
        while next(g)[-1] != 'Z':
            rounds += 1
        answer = (answer*rounds)//gcd(answer, rounds) # LCM
    print('Part 2-', answer)



cmd, dic= parse(file_path)
part2(cmd, dic)