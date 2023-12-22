#! /usr/bin/env python3

import aoc
import math

args = aoc.argparse()

class Brick:
    xmin = ymin = math.inf
    xmax = ymax = -math.inf

    def __init__(self, e1, e2):
        x1, y1, z1 = map(int, e1)
        x2, y2, z2 = map(int, e2)
        self.zlow = min(z1, z2)
        self.zhigh = max(z1, z2)
        xmin = min(x1, x2) ; Brick.xmin = min(Brick.xmin, xmin)
        xmax = max(x1, x2) ; Brick.xmax = max(Brick.xmax, xmax)
        ymin = min(y1, y2) ; Brick.ymin = min(Brick.ymin, ymin)
        ymax = max(y1, y2) ; Brick.ymax = max(Brick.ymax, ymax)
        self.map = [(x,y) for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)]
        self.supportedby = set()
        self.supports = set()

    def downto(self, z):
        dz = z - self.zlow
        assert dz <= 0
        self.zlow += dz
        self.zhigh += dz


bricks = [Brick(e1.split(','), e2.split(',')) for e1, e2 in aoc.Input(split='~')]

ground = Brick((Brick.xmin, Brick.ymin, 0), (Brick.xmax, Brick.ymax, 0))
top = {xy: ground for xy in ground.map}

for brick in sorted(bricks, key=lambda b:b.zlow):
    below = sorted((top[xy] for xy in brick.map), reverse=True, key=lambda b:b.zhigh)
    zsupport = below[0].zhigh
    for support in (b for b in below if b.zhigh == zsupport and b != ground):
        brick.supportedby.add(support)
        support.supports.add(brick)
    brick.downto(zsupport + 1)
    top.update({xy: brick for xy in brick.map})


if args.part == 1:
    count = 0
    for brick in bricks:
        for b in brick.supports:
            if len(b.supportedby) == 1:
                break
        else:
            count += 1
    print(count)
# solution: 416


if args.part == 2:
    count = 0
    for brick in bricks:
        fallen = set([brick])
        states = list(brick.supports)
        while states:
            state = states.pop(0)
            states.extend(b for b in state.supports if b not in states)
            if not (state.supportedby - fallen):
                fallen.add(state)
        count += len(fallen) - 1
    print(count)
# solution: 60963
