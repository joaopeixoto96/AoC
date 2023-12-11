import os
from copy import deepcopy as dp
file_path = os.path.join('Advent of Code 2023','day11.txt')

t = 0
rows = open(file_path).read().splitlines()

'''Part 1'''
# y = []
# for i in rows:
#     y.append(i)
#     if "#" not in i:
#         y.append(i)
# y = list(zip(*y))
# x=dp(y)
# y=[]
# for i in x:
#     y.append(i)
#     if "#" not in i:
#         y.append(i)
# x=dp(y)
# v=set()
# for i in range(len(x)):
#     for r in range(len(x[0])):
#         if x[i][r]=="#":
#             v.add((i,r))
# v=list(v)
# for i in range(len(v)):
#     for r in range(i+1,len(v)):
#         t+=abs(v[i][0]-v[r][0])+abs(v[i][1]-v[r][1])

# print('Part 1 -',t)



'''Part 2'''
x = rows
y = []

for i in range(len(x)):
    if "#" not in x[i]:
        y.append(i)


yy = []
for r in range(len(x[0])):
    for i in range(len(x)):
        if x[i][r] == "#":
            break
    else:
        yy.append(r)
v = set()
ii = 0
rr = 0
for i in range(len(x)):
    if i in y:
        ii += 1000000
        ii -= 1
    rr = 0
    for r in range(len(x[0])):
        if r in yy:
            rr += 1000000
            rr -= 1
        if x[i][r] == "#":
            v.add((i+ii,r+rr))

v=list(v)
for i in range(len(v)):
    for r in range(i+1,len(v)):
        t+=abs(v[i][0]-v[r][0])+abs(v[i][1]-v[r][1])

print('Part 2 -',t) 