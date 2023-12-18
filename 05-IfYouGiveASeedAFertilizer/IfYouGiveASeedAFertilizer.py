#! /usr/bin/env python3

import math
import aoc

args = aoc.argparse()


if args.part == 1:
    # Configure input to split line at blanks and convert item to int when possible
    input = aoc.Input(split=None, convert=int)

    # Read the first two lines. The first one gives the seed numbers
    items = dict(
        seed=list(next(input))[1:]
    )
    next(input)

    # In each paragraph of the almanac
    #  - the first line gives the source and the destination
    #  - the rest is the definition of the conversion function:
    #      piecewise linear function of a slope 1 where for each piece
    #       - the start of the ouput range,
    #       - the start of the input range and
    #       - the range length
    #      are given in that order
    input.groupby = 'paragraph'
    for paragraph in input:
        src, dst = next(paragraph)[0].split('-')[::2]
        converttable = list(paragraph)

        def convert(item):
            for dststart, srcstart, length in converttable:
                if item >= srcstart and item < srcstart + length:
                    return dststart + item - srcstart
            return item

        # apply conversion on the previous results (starting at seeds)
        lastlist = items[dst] = [convert(item) for item in items[src]]

    # all seed numbers have been converted to location numbers, the smallest of which is sought.
    print(min(lastlist))
# solution: 389056265


if args.part == 2:
    # Configure input to split line at blanks and convert item to int when possible
    input = aoc.Input(split=None, convert=int)

    # Read the first two lines. The first one gives the seed range of numbers (start, length),kept sorted by start number
    seedline = list(next(input))[1:]
    seedranges = sorted([(int(start), int(length)) for start, length in zip(seedline[::2], seedline[1::2])])
    print("                                        seeds")
    for seedstart, ln in seedranges:
        print(f"{' '*29}[{seedstart:10} - {seedstart + ln:10}]")
    print()
    next(input)

    # In each paragraph of the almanac
    #  - the first line gives the source and the destination
    #    this information is not kept as a quick view at the input file shows that the conversion are to be applied
    #    in order: seed-to-soil, soil-to-fertilizer, ..., humidity-to-location
    #  - the rest is the definition of the conversion function:
    #      piecewise linear function of a slope 1 where for each piece
    #       - the start of the ouput range,
    #       - the start of the input range and
    #       - the range length
    #      are given in that order
    #  A list of conversion tables is kept. Each table is sorted by start of output range
    input.groupby = 'paragraph'
    tables = []
    for paragraph in input:
        src, dst = next(paragraph)[0].split('-')[::2]
        tables.append(sorted(list(paragraph)))

    # It is not possible to convert all the seed values into locations to find the minimum since there are far too many.
    # The inverse function from location to seed is again a piecewise linear function of a slope 1. Computing each
    # piece range is possible. Starting at 0, the smallest possible location value (oh yes, by the way, each piecewise
    # linear function have a definition set of [0...[ and a image set also of [0...[) and incrementing until we find
    # a seed which is an antecedant of a location
    print()
    print("         location         <=            seed")
    found = False
    start = 0
    while not found:
        # Given a location value, compute the n inverse functions until reaching the seed antecedant value
        # At the same time, we calculate the length of the range of the piecewise global inverse function
        # => seed, length
        location = start
        print(f"[{start:10}", end="")
        length = math.inf
        for table in reversed(tables):
            for dst, src, ln in table:
                if dst + ln <= start:
                    continue
                if start < dst:
                    length = min(length, dst - start)
                    # start = start
                    break
                else:  # dst <= start < dst + ln
                    length = min(length, dst + ln - start)
                    start = src + (start - dst)
                    break
            else:
                # length = length
                # start = start
                pass
        seed = start
        if length:
            print(f" - {location + length - 1:10}] <= [{seed:10} - {seed + length - 1:10}]")
        else:
            print("] <= [{seed}]")

        # Find in range [seed, seed + length - 1] an initial seed value
        for seedstart, ln in seedranges:
            if seedstart + ln <= seed:
                continue
            if seedstart <= seed:
                found = True
                break
            if seedstart <= seed + length:
                found = True
                location += seedstart - seed
                seed = seedstart
                break
        else:
            # If not found, find again with a greater location value
            start = location + length
    print()
    print(f" {location:10}                <= {seed:10}")
# solution: 137516820
