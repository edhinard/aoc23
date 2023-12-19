#! /usr/bin/env python3

import itertools
import math
import re

import aoc

args = aoc.argparse()


# Infinite iterator of (L)eft / (R)ight instructions
input = aoc.Input()
instructions = itertools.cycle(next(input))

# empty line
next(input)

# Binary oriented graph where nodes made of (L)eft / (R)ight descendants are sorted by name
input.split = re.compile(r'(\w+) = \((\w+), (\w+)\)')
nodes = {node: dict(L=left, R=right) for node, left, right in input}


if args.part == 1:
    # Just walk the graph from AAA to ZZZ according to instructions and count the steps
    length = 0
    node = 'AAA'
    while node != 'ZZZ':
        instruction = next(instructions)
        node = nodes[node][instruction]
        length += 1

    print(length)
# solution: 14257


if args.part == 2:
    # Measure length of all graph walks from ..A to ..Z
    lengths = []
    for node in [n for n in nodes.keys() if n.endswith('A')]:
        instructions = itertools.cycle(next(aoc.Input()))
        length = 0
        while not node.endswith('Z'):
            instruction = next(instructions)
            node = nodes[node][instruction]
            length += 1
        lengths.append(length)

    # Result is the Least Common Multiple of all lengths
    print(math.lcm(*lengths))
# solution: 16187743689077
