#! /usr/bin/env python3
import aoc

args = aoc.argparse()

if args.part == 1:
    instructions = [(d, l) for d, l, x in aoc.Input(split=None, convert=int)]
# solution: 47045


if args.part == 2:
    # For this part instructions are encoded in hexa subtring
    instructions = []
    for _, _, c in aoc.Input(split=None):
        l = int(c[2:-2], base=16)
        d = {'0':'R', '1':'D', '2':'L', '3':'U'}[c[-2]]
        instructions.append((d, l))
# solution: 147839570293376

# The surface delimited by the closed loop is computed by parts
# when the digger moves from A to B, the surface increases by
#
#     OA x OB
#     -------
#        2
#
# where O is whatever point (origin is OK) and x is the cross product
# But that is only the surface delimited by the center of the digger. Complete
# with half digger width all around. Just add the half perimeter and 1. Easy.
x = y = 0
doublesurface = 0
perimeter = 0
for direction, length in instructions:
    Ax, Ay = x, y
    dx, dy = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}[direction]
    x += dx * length
    y += dy * length
    Bx, By = x, y
    doublesurface += (Ax * By) - (Ay * Bx)
    perimeter += length
print((abs(doublesurface) + perimeter) // 2 + 1)
