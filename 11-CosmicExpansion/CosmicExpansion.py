#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    mapr = []
    for row in aoc.Input().iter():
        mapr.append(row)
        if set(row) == set('.'):
            mapr.append(row)
    mapc = []
    for column in zip(*mapr):
        mapc.append(column)
        if set(column) == set('.'):
            mapc.append(column)
    galaxies = []
    for x, column in enumerate(mapc):
        for y, item in enumerate(column):
            if item == '#':
                galaxies.append((x, y))

    distance = 0
    for i, (xA, yA) in enumerate(galaxies[:-1]):
        for xB, yB in galaxies[i+1:]:
            distance += xB - xA + abs(yB - yA)
    print(distance)
# solution: 10165598


if args.part == 2:
    mapr = []
    rowsplits = []
    for j, row in enumerate(aoc.Input().iter()):
        mapr.append(row)
        if set(row) == set('.'):
            rowsplits.append(j)
    mapc = []
    columnsplits = []
    for i, column in enumerate(zip(*mapr)):
        mapc.append(column)
        if set(column) == set('.'):
            columnsplits.append(i)

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
                galaxies.append((c, deltac, r, deltar))

    distance = 0
    for i, (cA, dcA, rA, drA) in enumerate(galaxies[:-1]):
        for cB, dcB, rB, drB in galaxies[i+1:]:
            distance += cB - cA + (dcB - dcA) * (1000000 - 1) +\
                abs(rB - rA) + abs((drB - drA) * (1000000 - 1))
    print(distance)
# solution: 678728808158
