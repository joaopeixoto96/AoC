import os
import time
start = time.time()
file_path = os.path.join('AoC_2023','day21.txt')

G = {i + j*1j: c for i,r in enumerate(open(file_path))
                 for j,c in enumerate(r) if c in '.S'}

N = 131

done = []
todo = {x for x in G if G[x]=='S'}

for s in range(int(2.5*N)+1):
    if s == 64: print(len(todo))
    if s%N == N//2: done.append(len(todo))

    todo = {p+d for d in {1,-1,1j,-1j} for p in todo
            if (p+d).real%N + (p+d).imag%N*1j in G}

f = lambda n,a,b,c: a+n*(b-a) +n*(n-1)//2*((c-b)-(b-a))
print(f(26501365//N, *done))

end = time.time()
print(f'It took {end - start:.2f} s to run')