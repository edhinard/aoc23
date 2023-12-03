#! /usr/bin/env python3

import re

import aoc

args = aoc.argparse()


if args.part == 1:
    parts = set()
    for y, line in enumerate(aoc.Input().iter()):
        for x, cell in enumerate(line):
            if not cell.isdigit() and cell != '.':
                parts.add((x, y))
                
    sum = 0
    for y, line in enumerate(aoc.Input().iter()):
        for match in re.finditer(r'(\d+)', line):
            num = int(match.group(1))
            startx, endx = match.span(1)

            if (startx - 1, y) in parts or (endx, y) in parts:
                sum += num
                continue
            for x in range(startx - 1, endx + 1):
                if (x, y - 1) in parts or (x, y + 1) in parts:
                    sum += num
                    break
    print(sum)

# solution: 533775


if args.part == 2:
    gears = {}
    for y, line in enumerate(aoc.Input().iter()):
        for x, cell in enumerate(line):
            if cell == '*':
                gears[(x, y)] = [0, 1]

    def update(x, y, num):
        global gears
        count, mult = gears.get((x, y), [0, 0])
        if not mult:
            return
        count += 1
        mult *= num
        gears[x, y] = [count, mult]
                
    for y, line in enumerate(aoc.Input().iter()):
        for match in re.finditer(r'(\d+)', line):
            num = int(match.group(1))
            startx, endx = match.span(1)

            update(startx - 1, y, num)
            update(endx, y, num)
            for x in range(startx - 1, endx + 1):
                update(x, y - 1, num)
                update(x, y + 1, num)

    sum = 0
    for count, ratio  in gears.values():
        if count == 2:
            sum += ratio
    print(sum)
# solution: 78236071
