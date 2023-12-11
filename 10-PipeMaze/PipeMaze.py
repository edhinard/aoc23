#! /usr/bin/env python3

import aoc

args = aoc.argparse()


def cleanup(map):
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
    #  try the 4 possible directions
    for dX, dY, initialdir in ((1, 0, 'WE'), (0, 1, 'NS'), (-1, 0, 'EW'), (0, -1, 'SN')):
        looplen = 1
        loop = [[' '] * len(map[0]) for _ in range(len(map))]
        X, Y = start
        X += dX
        Y += dY
        dir = initialdir
        loop[Y][X] = pipe = map[Y][X]
        while (X, Y) != start:
            if X < 0 or X >= len(loop[0]) or Y < 0 or Y >= len(loop):
                # this is not a loop, wrong initial direction
                break
            match dir, pipe:
                case 'WE', '-':
                    X += 1
                case 'WE', '7':
                    Y += 1
                    dir = 'NS'
                case 'WE', 'J':
                    Y -= 1
                    dir = 'SN'

                case 'EW', '-':
                    X -= 1
                case 'EW', 'F':
                    Y += 1
                    dir = 'NS'
                case 'EW', 'L':
                    Y -= 1
                    dir = 'SN'

                case 'NS', '|':
                    Y += 1
                case 'NS', 'J':
                    X -= 1
                    dir = 'EW'
                case 'NS', 'L':
                    X += 1
                    dir = 'WE'

                case 'SN', '|':
                    Y -= 1
                case 'SN', '7':
                    X -= 1
                    dir = 'EW'
                case 'SN', 'F':
                    X += 1
                    dir = 'WE'

                case _:
                    break

            if loop[Y][X] != ' ':
                break
            loop[Y][X] = pipe = map[Y][X]
            looplen += 1

        if (X, Y) == start:
            # loop is closed replace pipe at Starting point
            S = dict(WEWE='-', WENS='L', WESN='F', SNSN='|', NSWE='7', EWNS='J')[f'{initialdir}{dir}']
            loop[Y][X] = S
            return loop, looplen


map = [line for line in aoc.Input()]
loop, looplen = cleanup(map)


if args.part == 1:
    print(looplen // 2)
# solution: 6882


if args.part == 2:
    count = 0
    for line in loop:
        inside = 0
        previous = ' '
        for pipe in line:
            if pipe == ' ':
                count += inside
                continue
            if pipe == '-':
                continue
            if previous + pipe not in ('L7', 'FJ'):
                inside = 1 - inside
            previous = pipe
    print(count)
# solution: 491
