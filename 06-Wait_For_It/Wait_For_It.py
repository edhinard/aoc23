#! /usr/bin/env python3

import dataclasses
import re
import math

print("Part 1")
times = map(int, "38     94     79     70".split())
distances = map(int, "241   1549   1074   1091".split())
res = 1
for time, distance in zip(times, distances):
    wins = 0
    for t in range(time):
        if t * (time - t) > distance:
            wins += 1
    res *= wins
print(res)
# solution: 1083852


print("\nPart 2")
time = 38947970
distance = 241154910741091
# -x2 + t.x - d = 0
delta = time**2 - 4 * distance
range = math.sqrt(delta) / 1
print(int(range))
# solution: 23501589
