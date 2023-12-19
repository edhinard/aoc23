#! /usr/bin/env python3

import aoc

args = aoc.argparse()


def predict(nums):
    # Build the differences list of input sequence
    # until all zeros
    diffs = [nums]
    while any(diffs[-1]):
        prev = diffs[-1]
        diff = [b - a for a, b in zip(prev[:-1], prev[1:])]
        diffs.append(diff)

    # The prediction is the sum of last number of all lists
    return sum((diff[-1] for diff in diffs))


if args.part == 1:
    print(sum((predict(nums) for nums in aoc.Input(split=None, convert=int))))
# solution: 1921197370


if args.part == 2:
    # Reverse the list to predict the past
    print(sum((predict(list(reversed(nums))) for nums in aoc.Input(split=None, convert=int))))
# solution: 1124
