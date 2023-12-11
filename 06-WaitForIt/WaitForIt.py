#! /usr/bin/env python3

import math
import aoc

args = aoc.argparse()


if args.part == 1:
    input = aoc.Input(split=None, convert=int)
    times = next(input)[1:]
    distances = next(input)[1:]
    res = 1
    for time, distance in zip(times, distances):
        wins = 0
        for t in range(time):
            if t * (time - t) > distance:
                wins += 1
        res *= wins
    print(res)
# solution: 1083852


if args.part == 2:
    input = aoc.Input(split=None)
    time = int(''.join(next(input)[1:]))
    distance = int(''.join(next(input)[1:]))
    # -x2 + t.x - d = 0
    delta = time**2 - 4 * distance
    range = math.sqrt(delta) / 1
    print(int(range))
# solution: 23501589
