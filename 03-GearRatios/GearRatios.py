#! /usr/bin/env python3

import re
import aoc

args = aoc.argparse()


if args.part == 1:
    # Go through the input schematic a first time to get location of parts
    # that is chars that are not digit nor dot. Location are (x, y) tuple
    # where x is the column number (starting 0) and y the line number (starting 0)
    parts = set()
    for y, line in enumerate(aoc.Input()):
        for x, cell in enumerate(line):
            if not cell.isdigit() and cell != '.':
                parts.add((x, y))

    # Go through the input schematic a second time looking for continuous
    # sequence of digits (regular expression \d+) whose value, start and end
    # position in the line are retained
    sum = 0
    for y, line in enumerate(aoc.Input()):
        for match in re.finditer(r'(\d+)', line):
            value = int(match.group(1))
            start, end = match.span(1)

            # Look around the digit sequence for a part
            #  - before the sequence (same line y, position start -1) or
            #    after (same line y, position end)
            #  - in lines above (y - 1) and below (y + 1), x in [start-1, end]
            # Accumulate value once an adjacent part is found
            if (start - 1, y) in parts or (end, y) in parts:
                sum += value
                continue
            for x in range(start - 1, end + 1):
                if (x, y - 1) in parts or (x, y + 1) in parts:
                    sum += value
                    break

    print(sum)
# solution: 533775


if args.part == 2:
    class Gear:
        locations = {}

        def __init__(self):
            self.count = 0
            self.ratio = 1

        @staticmethod
        def findandupdate(x, y, value):
            if (x, y) not in Gear.locations:
                return
            gear = Gear.locations[(x, y)]
            gear.count += 1
            gear.ratio *= value        

    # Go through the input schematic a first time to get the gears (star symbol)
    # sorted by their location (column number, line number).
    for y, line in enumerate(aoc.Input()):
        for x, cell in enumerate(line):
            if cell == '*':
                Gear.locations[(x, y)] = Gear()

    # Go through the input schematic a second time looking for continuous
    # sequence of digits (regular expression \d+) whose value, start and end
    # position in the line are retained
    for y, line in enumerate(aoc.Input()):
        for match in re.finditer(r'(\d+)', line):
            value = int(match.group(1))
            start, end = match.span(1)

            # Look around the digit sequence for a gear
            #  - before the sequence (same line y, position start -1) or
            #    after (same line y, position end)
            #  - in lines above (y - 1) and below (y + 1), x in [start-1, end]
            # Each time a gear is found it is updated, that is its counter
            # (initial value 0) is incremented and its ratio (initial value 1)
            # is multiplied by value
            Gear.findandupdate(start - 1, y, value)
            Gear.findandupdate(end, y, value)
            for x in range(start - 1, end + 1):
                Gear.findandupdate(x, y - 1, value)
                Gear.findandupdate(x, y + 1, value)

    # Accumulate the ratio of gears whose count is 2 (others are not gear)
    print(sum((gear.ratio for gear in Gear.locations.values() if gear.count == 2)))
# solution: 78236071
