#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    map = [line for line in aoc.Input().iter()]
    for y, line in enumerate(map):
        for x, pipe in enumerate(line):
            if pipe == 'S':
                start = (x, y)
                break
        else:
            continue
        break
    # cheat: S is '-', look at the input
    count = 1
    X = start[0] + 1
    Y = start[1]
    dir = 'WE'
    while (X, Y) != start:
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

        count += 1
        pipe = map[Y][X]
                
    print(count // 2)
# solution: 6882


if args.part == 2:
    map = [line for line in aoc.Input().iter()]
    for y, line in enumerate(map):
        for x, pipe in enumerate(line):
            if pipe == 'S':
                start = (x, y)
                break
        else:
            continue
        break
    X, Y  = start
    loop = [[' '] * len(map[0]) for _ in range(len(map))]
    loop[Y][X] = '-'
    dir = 'WE'
    X += 1
    while (X, Y) != start:
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

        pipe = map[Y][X]
        loop[Y][X] = pipe

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

