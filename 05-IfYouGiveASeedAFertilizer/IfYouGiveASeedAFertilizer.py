#! /usr/bin/env python3

import math
import aoc

args = aoc.argparse()


if args.part == 1:
    input = aoc.Input(split=None, convert=int)

    items = dict(
        seed=list(next(input))[1:]
    )
    next(input)

    input.groupby = 'paragraph'
    for paragraph in input:
        src, dst = next(paragraph)[0].split('-')[::2]
        converttable = list(paragraph)

        def convert(item):
            for dststart, srcstart, length in converttable:
                if item >= srcstart and item < srcstart + length:
                    return dststart + item - srcstart
            return item
        lastlist = items[dst] = [convert(item) for item in items[src]]
    print(min(lastlist))
# solution: 389056265


if args.part == 2:
    input = aoc.Input(split=None, convert=int)

    seedline = list(next(input))[1:]
    seedranges = sorted([(int(start), int(length)) for start, length in zip(seedline[::2], seedline[1::2])])
    print("                                        seeds")
    for seedstart, ln in seedranges:
        print(f"{' '*29}[{seedstart:10} - {seedstart + ln:10}]")
    print()
    next(input)

    input.groupby = 'paragraph'
    tables = []
    for paragraph in input:
        src, dst = next(paragraph)[0].split('-')[::2]
        tables.append(sorted(list(paragraph)))

    print()
    print("         location         <=            seed")
    found = False
    start = 0
    while not found:
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
            start = location + length
    print()
    print(f" {location:10}                <= {seed:10}")
# solution: 137516820
