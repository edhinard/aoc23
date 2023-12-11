#! /usr/bin/env python3

import aoc

args = aoc.argparse(winningslen=10)


if args.part == 1:
    sum = 0
    for line in aoc.Input(split=None):
        win = set(line[2:2 + args.winningslen])
        got = set(line[3 + args.winningslen:])
        nummatches = len(win & got)
        if nummatches:
            sum += 2 ** (nummatches - 1)
    print(sum)
# solution: 21558


if args.part == 2:
    lines = list(aoc.Input(split=None))
    cards = [1] * len(lines)
    for currentcard, copies in enumerate(cards):
        line = lines[currentcard]
        win = set(line[2:2 + args.winningslen])
        got = set(line[3 + args.winningslen:])
        nummatches = len(win & got)
        for i in range(nummatches):
            cards[currentcard + i + 1] += copies
    print(sum(cards))
# solution: 10425665
