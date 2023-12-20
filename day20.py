import os
import math
from typing import List
import functools
file_path = os.path.join('AoC_2023','day20.txt')

def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            split = line.split(" -> ")

            name = split[0]
            flip_flop = name.startswith("%")
            conjunction = name.startswith("&")
            target = split[1].split(", ")

            if flip_flop:
                state = False
                name = split[0][1:]
            elif conjunction:
                state = {}
                name = split[0][1:]
            else:
                state = None

            val = (name, [target, flip_flop, conjunction, state])

            lines.append(val)

    return lines


def part_one():
    lines = read_lines_to_list()
    mappings = dict((a, b) for (a, b) in lines)

    # For any conjunction modules we must initialize inputs...
    for k, v in mappings.items():
        if v[2]:
            for a, b in mappings.items():
                if k in b[0]:
                    v[3][a] = False

    low = 0
    high = 0
    for _ in range(1000):
        queue = [("broadcaster", 0, None)]
        while queue:
            (curr, signal, input) = queue.pop(0)

            if signal:
                high += 1
            else:
                low += 1

            if curr not in mappings:
                continue

            [targets, is_ff, is_con, state] = mappings[curr]

            if is_ff:
                if not signal:
                    if state:
                        mappings[curr][3] = False
                        new_signal = 0
                    else:
                        mappings[curr][3] = True
                        new_signal = 1

                    for target in targets:
                        queue.append((target, new_signal, curr))
            elif is_con:
                state[input] = bool(signal)
                if all(state.values()):
                    new_signal = 0
                else:
                    new_signal = 1
                for target in targets:
                    queue.append((target, new_signal, curr))
            else:
                for target in targets:
                    queue.append((target, signal, curr))

    answer = low * high
    print(f"Part 1 - {answer}")



part_one()


m = {}
f = {}
c = {}
for l in open(file_path):
    s, *d = l.replace( ',', '' ).replace( "->", "" ).split()
    t = None
    if s != "broadcaster":
        t = s[ 0 ]
        s = s[ 1 : ]
    m[ s ] = ( t, d )
    f[ s ] = "off"
    for o in d:
        if o not in c:
            c[ o ] = {}
        c[ o ][ s ] = "low"
    if d == [ 'rx' ]:
        r = s

b = 0
l = { k: 0 for k in c[ r ] }
while True:
    b += 1
    q = [ ( "button", "broadcaster", "low" )  ]
    while q:
        i, n, p = q.pop( 0 )
        if n not in m:
            continue
        t, d = m[ n ]
        if t == None:
            for o in d:
                q.append( ( n, o, p ) )
        elif t == '%':
            if p == "low":
                s = f[ n ]
                if s == "off":
                    f[ n ] = "on"
                    for o in d:
                        q.append( ( n, o, "high" ) )
                else:
                    f[ n ] = "off"
                    for o in d:
                        q.append( ( n, o, "low" ) )
        elif t == '&':
            c[ n ][ i ] = p
            if all( v == "high" for v in c[ n ].values() ):
                for o in d:
                    q.append( ( n, o, "low" ) )
            else:
                for o in d:
                    q.append( ( n, o, "high" ) )
            if n == r:
                for k, v in c[ n ].items():
                    if v == "high" and l[ k ] == 0:
                        l[ k ] = b
    if all( v > 0 for v in l.values() ):
        print('Part 2 -', functools.reduce( ( lambda a, b: a * b ), l.values() ) )
        break