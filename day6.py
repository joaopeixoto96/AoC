import os
import numpy as np
file_path = os.path.join('Advent of Code 2023','day6.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    boats = [entry.strip() for entry in lines]



race_times = list(boats[0].split())
race_times.pop(0)
race_records = list(boats[1].split())
race_records.pop(0)

'''Part 1 - uncomment for results'''
# wins = []
# for race in range(len(race_times)):
#     race_time = int(race_times[race])
#     race_record = int(race_records[race])
#     race_dist = []
#     for t_mov in range(race_time+1):
#         t_charge = race_time - t_mov
#         vel = t_charge
#         dist = vel * t_mov
#         if dist > race_record:
#             race_dist.append(dist)
#     wins.append(len(race_dist))

# print(np.prod(wins))

'''Part 2 - uncomment for results'''
wins = []
race_time = int(''.join(map(str, race_times)))
race_record = int(''.join(map(str, race_records)))
race_dist = []
for t_mov in range(race_time+1):
    t_charge = race_time - t_mov
    vel = t_charge
    dist = vel * t_mov
    if dist > race_record:
        race_dist.append(dist)
wins.append(len(race_dist))
print(np.prod(wins))
