import os
file_path = os.path.join('Advent of Code 2023','day9.txt')
lines = open(file_path).read().splitlines()

def part1(a):
  if a[0] == a[1] == a[-1]:
    return a[-1]
  return a[-1] + part1([a[i]-a[i-1] for i in range(1,len(a))])

def part2(a):
  if a[0] == a[1] == a[-1]:
    return a[0]
  return a[0] - part2([a[i]-a[i-1] for i in range(1,len(a))])

result_1 = sum(part1([int(item) for item in line.split()]) for line in lines)
print('Part 1 -',result_1)

result_2 = sum(part2([int(item) for item in line.split()]) for line in lines)
print('Part 2 -',result_2)