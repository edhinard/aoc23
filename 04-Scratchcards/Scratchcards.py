#! /usr/bin/env python3

import re

import aoc

args = aoc.argparse()


if args.part == 1:
    sum = 0
    for line in aoc.Input().iter():
        numbers = re.findall(r'(\d+)', line)
        win = set(numbers[1:11])
        got = set(numbers[11:])
        nummatches = len(win & got)
        if nummatches:
            sum += 2 ** (nummatches - 1)
    print(sum)

# solution: 21558


if args.part == 2:
    lines = aoc.Input().list()
    cards = [1] * len(lines)
    for currentcard, copies in enumerate(cards):
        line = lines[currentcard]
        numbers = re.findall(r'(\d+)', line)
        win = set(numbers[1:11])
        got = set(numbers[11:])
        nummatches = len(win & got)        
        for i in range(nummatches):
            cards[currentcard + i + 1] += copies
    print(sum(cards))

# solution: 10425665
