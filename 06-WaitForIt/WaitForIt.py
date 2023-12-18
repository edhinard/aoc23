#! /usr/bin/env python3

import math
import aoc

args = aoc.argparse()


if args.part == 1:
    # Read a list of times and a list of records
    input = aoc.Input(split=None, convert=int)
    times = next(input)[1:]
    records = next(input)[1:]

    # Try all solution t in range [0, time - 1]
    #  for each, compare with best distance reach (the record), count the number of time the record can be beat
    res = 1
    for time, record in zip(times, records):
        wins = 0
        for t in range(time):
            if t * (time - t) > record:
                wins += 1
        res *= wins

    # result is the product of all counts
    print(res)
# solution: 1083852


if args.part == 2:
    # Read a single time and record value
    input = aoc.Input(split=None)
    time = int(''.join(next(input)[1:]))
    record = int(''.join(next(input)[1:]))

    # No need to compute all t values. The distance above the record is a quadratic function of t:
    #         2
    #   d = -t  + time.t - record
    # whose values are positive inside the two roots (when they exist)
    #         2
    # Δ = time  - 4.record
    #             _
    # t2 - t1 = \/Δ
    delta = time**2 - 4 * record
    print(int(math.sqrt(delta)))
# solution: 23501589
