#! /usr/bin/env python3

import aoc

args = aoc.argparse(expansion=1000000)


if args.part == 1:
    expansion = 2
# solution: 10165598


if args.part == 2:
    expansion = args.expansion
# solution: 678728808158


mapr = []
rowsplits = []
for r, row in enumerate(aoc.Input()):
    mapr.append(row)
    if set(row) == set('.'):
        rowsplits.append(r)
mapc = []
columnsplits = []
for c, column in enumerate(zip(*mapr)):
    mapc.append(column)
    if set(column) == set('.'):
        columnsplits.append(c)

galaxies = []
deltac = 0
for c, column in enumerate(mapc):
    if c in columnsplits:
        deltac += 1
    deltar = 0
    for r, item in enumerate(column):
        if r in rowsplits:
            deltar += 1
        if item == '#':
            galaxies.append((c + deltac * (expansion - 1), r + deltar * (expansion - 1)))

distance = 0
for i, (cA, rA) in enumerate(galaxies[:-1]):
    for cB, rB in galaxies[i+1:]:
        distance += cB - cA + abs(rB - rA)
print(distance)
