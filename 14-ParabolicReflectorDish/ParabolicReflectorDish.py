#! /usr/bin/env python3

import aoc

args = aoc.argparse()

if args.part == 1:
    def load(column):
        stop = len(column)
        load = 0
        for i, rock in enumerate(column, start=1):
            if rock == '#':
                stop = len(column) - i
            elif rock == 'O':
                load += stop
                stop -= 1
        return load

    rows = [row for row in aoc.Input()]
    num = sum(load(column) for column in zip(*rows))
    print(num)
# solution: 113486


if args.part == 2:
    def tilt(platform):
        lines = []
        for line in zip(*platform.split('\n')):
            lines.append(['.'] * len(line))
            stop = len(line)
            for i, rock in enumerate(line, start=1):
                if rock == '#':
                    stop = len(line) - i
                    lines[-1][stop] = '#'
                elif rock == 'O':
                    stop -= 1
                    lines[-1][stop] = 'O'
        return '\n'.join(''.join(line) for line in lines)

    def load(platform):
        load = 0
        for line in zip(*platform.split('\n')):
            for i, rock in enumerate(line):
                if rock == 'O':
                    load += len(line) - i
        return load
        
    platform = aoc.Input().read().strip()
    platforms = dict()
    loads = []
    for cycle in range(1000000000):
        platforms[platform] = cycle
        loads.append(load(platform))

        for _ in range(4):
            platform = tilt(platform)

        if platform in platforms:
            break

    start = platforms[platform]
    period = cycle - start + 1 # /!\ added the +1 to get the right result on test vector. don't understand
    end = start + (1000000000 - start) % period
    print(loads[end])
# solution: 104409
