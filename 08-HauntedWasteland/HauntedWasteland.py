#! /usr/bin/env python3

import itertools
import math
import re

import aoc

args = aoc.argparse()


if args.part == 1:
    input = aoc.Input()
    instructions = itertools.cycle(next(input))
    next(input)
    input.split = re.compile(r'(\w+) = \((\w+), (\w+)\)')
    nodes = {node: dict(L=left, R=right) for node, left, right in input}

    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        instruction = next(instructions)
        node = nodes[node][instruction]
        count += 1

    print(count)
# solution: 14257


if args.part == 2:
    input = aoc.Input()
    next(input)
    next(input)
    input.split = re.compile(r'(\w+) = \((\w+), (\w+)\)')
    nodes = {node: dict(L=left, R=right) for node, left, right in input}

    counts = []
    for node in [n for n in nodes.keys() if n.endswith('A')]:
        instructions = itertools.cycle(next(aoc.Input()))
        count = 0
        while not node.endswith('Z'):
            instruction = next(instructions)
            node = nodes[node][instruction]
            count += 1
        counts.append(count)
    print(math.lcm(*counts))
# solution: 16187743689077
