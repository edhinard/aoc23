#! /usr/bin/env python3

import aoc

args = aoc.argparse()

def hash(string):
    h = 0
    for c in string:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

if args.part == 1:
    print(sum(hash(step) for step in aoc.Input().read().strip().split(',')))
# solution: 511416


if args.part == 2:
    boxes = [dict() for _ in range(256)]
    for step in aoc.Input().read().strip().split(','):
        if step.endswith('-'):
            label = step[:-1]
            focal = None
        else:
            label, eq, focal = step.partition('=')
        h = hash(label)
        if focal is None:
            boxes[h].pop(label, None)
        else:
            boxes[h][label] = int(focal)
    print(sum(numbox * numlens * focal for numbox, box in enumerate(boxes, start=1) for numlens, (lens, focal) in enumerate(box.items(), start=1)))
# solution: 290779
