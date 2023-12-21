#! /usr/bin/env python3

import collections
import re

import aoc

args = aoc.argparse()

if args.part == 1:
    Beam = collections.namedtuple('Beam', 'x y dx dy')
    mirrors = [line for line in aoc.Input()]
    energized = set([(0,0)])
    firstbeam = Beam(0, 0, +1, 0)
    stack = [firstbeam]
    seen = [firstbeam]

    def addbeam(x, y, dx, dy):
        nx = x + dx
        ny = y + dy
        beam = Beam(nx, ny, dx, dy)
        if nx >= 0 and nx < len(mirrors[0]) and ny >= 0 and ny < len(mirrors) and beam not in seen:
            seen.append(beam)
            stack.append(beam)
            energized.add((nx, ny))

    while stack:
        x, y, dx, dy = stack.pop(0)
        mirror = mirrors[y][x]
        match dx, dy, mirror:
            case (_, _, '.') | (_, 0, '-') | (0, _, '|'):
                addbeam(x, y, dx, dy)
                
            case (_, 0, '|'):
                addbeam(x, y, 0, -1)
                addbeam(x, y, 0, +1)

            case (0, _, '-'):
                addbeam(x, y, -1, 0)
                addbeam(x, y, +1, 0)

            case (1, 0, '/') | (-1, 0, '\\'):
                addbeam(x, y, 0, -1)
            case (1, 0, '\\') | (-1, 0, '/'):
                addbeam(x, y, 0, +1)

            case (0, 1, '/') | (0, -1, '\\'):
                addbeam(x, y, -1, 0)
            case (0, 1, '\\') | (0, -1, '/'):
                addbeam(x, y, +1, 0)

    print(len(energized))
                
# solution: 6816


if args.part == 2:
    Beam = collections.namedtuple('Beam', 'x y dx dy')
    mirrors = [line for line in aoc.Input()]

    def conf(ix, iy, idx, idy):
        energized = set([(ix,iy)])
        firstbeam = Beam(ix, iy, idx, idy)
        stack = [firstbeam]
        seen = [firstbeam]

        def addbeam(x, y, dx, dy):
            nx = x + dx
            ny = y + dy
            beam = Beam(nx, ny, dx, dy)
            if nx >= 0 and nx < len(mirrors[0]) and ny >= 0 and ny < len(mirrors) and beam not in seen:
                seen.append(beam)
                stack.append(beam)
                energized.add((nx, ny))

        while stack:
            x, y, dx, dy = stack.pop(0)
            mirror = mirrors[y][x]
            match dx, dy, mirror:
                case (_, _, '.') | (_, 0, '-') | (0, _, '|'):
                    addbeam(x, y, dx, dy)

                case (_, 0, '|'):
                    addbeam(x, y, 0, -1)
                    addbeam(x, y, 0, +1)

                case (0, _, '-'):
                    addbeam(x, y, -1, 0)
                    addbeam(x, y, +1, 0)

                case (1, 0, '/') | (-1, 0, '\\'):
                    addbeam(x, y, 0, -1)
                case (1, 0, '\\') | (-1, 0, '/'):
                    addbeam(x, y, 0, +1)

                case (0, 1, '/') | (0, -1, '\\'):
                    addbeam(x, y, -1, 0)
                case (0, 1, '\\') | (0, -1, '/'):
                    addbeam(x, y, +1, 0)
        return len(energized)

    xmax = len(mirrors[0])
    ymax = len(mirrors)
    print(
        max(
            max(conf(x, 0, 0, +1) for x in range(xmax)),
            max(conf(x, ymax - 1, 0, -1) for x in range(xmax)),
            max(conf(0, y, +1, 0) for y in range(ymax)),
            max(conf(0, y, -1, 0) for y in range(ymax))
        )
    )
# solution: 8163
