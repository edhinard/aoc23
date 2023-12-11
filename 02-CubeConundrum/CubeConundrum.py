#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    sum = 0
    for line in aoc.Input():
        game, sets = line.split(':')
        num = int(game.split()[1])
        ok = True
        for set in sets.split(';'):
            for content in set.split(','):
                count, color = content.split()
                count = int(count)
                if color == 'red' and count > 12:
                    ok = False
                if color == 'green' and count > 13:
                    ok = False
                if color == 'blue' and count > 14:
                    ok = False
        if ok:
            sum += num
    print(sum)
# solution: 2632


if args.part == 2:
    sum = 0
    for line in aoc.Input():
        game, sets = line.split(':')
        num = int(game.split()[1])
        red = green = blue = 0
        for set in sets.split(';'):
            for content in set.split(','):
                count, color = content.split()
                count = int(count)
                if color == 'red':
                    red = max(red, count)
                if color == 'green':
                    green = max(green, count)
                if color == 'blue':
                    blue = max(blue, count)
        sum += red * green * blue
    print(sum)
# solution: 69629
