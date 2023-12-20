import os
import re

file_path = os.path.join('AoC_2023','day3.txt')
# with open(file_path, 'r') as f:
#     lines = f.readlines()
#     schematic = [entry.strip() for entry in lines]

import math as m


board = list(open(file_path))

chars = {(r, c): [] for r in range(len(board)) for c in range(len(board))
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))




'''Tentativa futil de ir item a item no ciclo... Today Reddit came in clutch I guess muito mais facil enunciar
os numeros que estamos a procura em vez de tentar adivinhar os chars especiais todos.'''
# def find_special(matrix):
#     special_chars = "!@#$%^&*()[]{}/;:,<>?|`~=+-_"
#     all_numbers = []
#     for i in range(len(matrix)):
#         j = 0
#         while j < len(matrix[i]):
#             if matrix[i][j].isdigit():
#                 num = ""
#                 while j < len(matrix[i]) and matrix[i][j].isdigit():
#                     num += matrix[i][j]
#                     j += 1                    
                
#                 neighbors = []
#                 for k in range(max(0, i - 1), min(len(matrix), i + 2)):
#                     for l in range(max(0, j - len(num)), min(len(matrix[i]), j + len(num))):
#                         if matrix[k][l] in special_chars:
#                             neighbors.append(matrix[k][l])
#                 if not any(neighbors):
#                     all_numbers.append(int(num))
#             else:
#                 j += 1
#     return all_numbers

# total = find_special(schematic)
# print(total)
    
