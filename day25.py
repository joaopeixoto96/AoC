import os
import time
import collections as C
start = time.time()
file_path = os.path.join('AoC_2023','day25.txt')
G = C.defaultdict(set)
for line in open(file_path):
    u, *vs = line.replace(':','').split()
    for v in vs: G[u].add(v); G[v].add(u)

S = set(G)
count = lambda v: len(G[v]-S)
while sum(map(count, S)) != 3:
    S.remove(max(S, key=count))
print(len(S) * len(set(G)-S))

end = time.time()
print(f'It took {end - start:.2f} s to run')