#! /usr/bin/env python3

import dataclasses
import sys

import aoc

args = aoc.argparse()


if args.part == 1:
    pass
# test:
# solution:


if args.part == 2:
    pass
# test:
# solution:


sys.exit(0)
@dataclasses.dataclass
class Monkey:
    value: None = None
    left: None = None
    right: None = None
    op: None = None


text = aoc.Input().read()

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
for sensorx, sensory, beaconx, beacony in aoc.Input().iter(
        split=re.compile(r'Sensor at x=([-]?\d+), y=([-]?\d+): closest beacon is at x=([-]?\d+), y=([-]?\d+)'),
        convert=int):
    pass

# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
paths = aoc.Input().list(split=' -> ', convert=lambda c: tuple(map(int, c.split(','))))

# A
# B
# C
# A
# B
# C
for a, b, c in aoc.Input().iter(groupby=3):
    pass

# 123
# 456
# 798
#
# 123
#
# 123
# 456
for paragraph in aoc.Input().iter(split='', convert=int, groupby='paragraph'):
    for n1, n2, n3 in paragraph:
        pass
