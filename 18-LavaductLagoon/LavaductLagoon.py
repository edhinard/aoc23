#! /usr/bin/env python3
import aoc

args = aoc.argparse()

if args.part == 1:
    instructions = [(d, l) for d, l, x in aoc.Input(split=None, convert=int)]
# solution: 47045


if args.part == 2:
    instructions = []
    for x, y, c in aoc.Input(split=None):
        l = int(c[2:-2], base=16)
        d = {'0':'R', '1':'D', '2':'L', '3':'U'}[c[-2]]
        instructions.append((d, l))
# solution: 147839570293376


X = Y = 0
S = 0
for direction, length in instructions:
    Ux, Uy = X, Y
    dx, dy = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}[direction]
    X += dx * length
    Y += dy * length
    Vx, Vy = X, Y
    S += (Ux * Vy) - (Uy * Vx) + length
print(int(S / 2 + 1))
