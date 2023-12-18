#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    sum = 0
    for line in aoc.Input():
        # split line at colon
        # extract game number from the left part
        # keep the right part (the list of subsets)
        game, subsets = line.split(':')
        num = int(game.split()[1])

        # split the right part at semicolons to get subsets
        #   split the subset at comas to get content
        #     split the content at blank to get a count and a color
        # a game is possible unless there are more than 12 red, 13 green or 14 blue
        possible = True
        for subset in subsets.split(';'):
            for content in subset.split(','):
                count, color = content.split()
                count = int(count)
                if color == 'red' and count > 12:
                    possible = False
                if color == 'green' and count > 13:
                    possible = False
                if color == 'blue' and count > 14:
                    possible = False

        # accululate game number of possible games
        if possible:
            sum += num

    print(sum)
# solution: 2632


if args.part == 2:
    sum = 0
    for line in aoc.Input():
        # split line at colon
        # extract game number from the left part
        # keep the right part (the list of subsets)
        game, subsets = line.split(':')
        num = int(game.split()[1])

        # split the right part at semicolons to get subsets
        #   split the subset at comas to get content
        #     split the content at blank to get a count and a color
        # compute the max number of each color (0 being the default)
        red = green = blue = 0
        for subset in subsets.split(';'):
            for content in subset.split(','):
                count, color = content.split()
                count = int(count)
                if color == 'red':
                    red = max(red, count)
                if color == 'green':
                    green = max(green, count)
                if color == 'blue':
                    blue = max(blue, count)

        # accululate the product of the computed maximums (the power of a set)
        sum += red * green * blue

    print(sum)
# solution: 69629
