#! /usr/bin/env python3

import dataclasses
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
    @dataclasses.dataclass
    class Gear:
        count: int = 0
        ratio: int = 1

    gears = {}
    for y, line in enumerate(aoc.Input().iter()):
        for x, cell in enumerate(line):
            if cell == '*':
                gears[(x, y)] = Gear()

    def updategear(x, y, num):
        global gears
        if (x, y) not in gears:
            return
        gear = gears[(x, y)]
        gear.count += 1
        gear.ratio *= num
                
    for y, line in enumerate(aoc.Input().iter()):
        for match in re.finditer(r'(\d+)', line):
            num = int(match.group(1))
            startx, endx = match.span(1)

            updategear(startx - 1, y, num)
            updategear(endx, y, num)
            for x in range(startx - 1, endx + 1):
                updategear(x, y - 1, num)
                updategear(x, y + 1, num)

    print(sum((gear.ratio for gear in gears.values() if gear.count == 2)))

# solution: 78236071
