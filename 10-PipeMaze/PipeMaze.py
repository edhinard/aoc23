#! /usr/bin/env python3

import aoc

args = aoc.argparse()


map = [line for line in aoc.Input()]

# find the Starting point
for y, line in enumerate(map):
    for x, pipe in enumerate(line):
        if pipe == 'S':
            start = (x, y)
            break
    else:
        continue
    break

# walk the path from start until the loop is closed
#  try the 4 possible directions (3 is enough n fact)
#  build a clean up map (called loop) while walking with only the necessary pipes
#  also count loop length
for direction in ('>', 'v', '<'):
    try:
        loop = [[' '] * len(map[0]) for _ in range(len(map))]
        initialdir = direction
        looplen = 1
        X, Y = start
        dX, dY = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1)}[direction]
        X += dX
        Y += dY
        loop[Y][X] = pipe = map[Y][X]
        while (X, Y) != start:
            direction = {'>-': '>', '>7': 'v', '>J': '^',
                         '<-': '<', '<F': 'v', '<L': '^',
                         'v|': 'v', 'vJ': '<', 'vL': '>',
                         '^|': '^', '^7': '<', '^F': '>'}[f'{direction}{pipe}']
            dX, dY = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}[direction]
            X += dX
            Y += dY
            if loop[Y][X] != ' ':
                raise Exception()
            loop[Y][X] = pipe = map[Y][X]
            looplen += 1

        if (X, Y) == start:
            # loop is closed replace pipe at Starting point
            S = {'>>': '-', '>^': 'F', '>v': 'L',
                 'vv': '|', 'v>': '7', 'v<': 'F',
                 '<<': '-', '<^': '7', '<v': 'J'}[f'{initialdir}{direction}']
            loop[Y][X] = S
            BREAK
    except:
        # this is not a loop
        continue


if args.part == 1:
    print(looplen // 2)
# solution: 6882


if args.part == 2:
    count = 0
    # traverse the clean up map horizontally at each line
    # starting outside, switch outside/inside each time a pipe
    #  with vertical end is encountered (every not empty, not horizontal pipe)
    # count inside empty cells
    for line in loop:
        inside = 0
        previous = ' '
        for cell in line:
            if cell == ' ':
                count += inside
                continue
            if cell == '-':
                continue
            if previous + cell not in ('L7', 'FJ'):
                inside = 1 - inside
            previous = cell
    print(count)
# solution: 491
