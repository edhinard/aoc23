#! /usr/bin/env python3

import aoc

args = aoc.argparse()


# Build the list of galaxies with their coordinate in sky map (row, column)
# in the same time mark the empty rows and columns (without any galaxy)
map = [line for line in aoc.Input()]
galaxies = []
rows = ['.'] * len(map)
columns = ['.'] * len(map[0])
for row, line in enumerate(map):
    for column, item in enumerate(line):
        if item == '#':
            galaxies.append((row, column))
            rows[row] = '#'
            columns[column] = '#'
rows = ''.join(rows)
columns = ''.join(columns)


if args.part == 1:
    expansion = 2
# solution: 10165598


if args.part == 2:
    expansion = 1000000 if not aoc.TEST else 100
# solution: 678728808158


# Take the number of empty rows and columns between each galaxy
# into account for distance computation
distance = 0
for i, A in enumerate(galaxies[:-1]):
    for B in galaxies[i+1:]:
        r1, r2 = sorted([A[0], B[0]])
        c1, c2 = sorted([A[1], B[1]])
        distance += \
            r2 - r1 + (expansion - 1) * rows.count('.', r1, r2 + 1) +\
            c2 - c1 + (expansion - 1) * columns.count('.', c1, c2 + 1)
print(distance)
