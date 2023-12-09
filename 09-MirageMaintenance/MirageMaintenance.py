#! /usr/bin/env python3

import itertools
import operator

import aoc

args = aoc.argparse()


if args.part == 1:
    res = 0
    for nums in aoc.Input().iter(split=None, convert=int):
        diffs = [nums]
        while any(diffs[-1]):
            prev = diffs[-1]
            diff = [b - a for a, b in zip(prev[:-1], prev[1:])]
            diffs.append(diff)
        res += sum((diff[-1] for diff in diffs))
    print(res)
# solution: 1921197370


if args.part == 2:
    res = 0
    for nums in aoc.Input().iter(split=None, convert=int):
        diffs = [nums]
        while any(diffs[-1]):
            prev = diffs[-1]
            diff = [b - a for a, b in zip(prev[:-1], prev[1:])]
            diffs.append(diff)
        extra = 0
        for diff in reversed(diffs):
            extra = diff[0] - extra
        res += extra
    print(res)
# solution: 1124
