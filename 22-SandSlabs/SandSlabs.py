#! /usr/bin/env python3

import aoc

args = aoc.argparse()

class Brick:
    def __init__(self, e1, e2):
        x1, y1, z1 = map(int, e1)
        x2, y2, z2 = map(int, e2)
        self.zlow = min(z1, z2)
        self.height = max(z1, z2) - self.zlow + 1
        self.xmin = min(x1, x2)
        self.xmax = max(x1, x2)
        self.ymin = min(y1, y2)
        self.ymax = max(y1, y2)
        self.map = [(x,y) for x in range(self.xmin, self.xmax + 1) for y in range(self.ymin, self.ymax + 1)]
        self.supportedby = set()
        self.supports = set()

bricks = [Brick(e1.split(','), e2.split(',')) for e1, e2 in aoc.Input(split='~')]

xmin = min(b.xmin for b in bricks)
xmax = max(b.xmax for b in bricks)
ymin = min(b.ymin for b in bricks)
ymax = max(b.ymax for b in bricks)
ground = Brick((xmin, ymin, 0), (xmax, ymax, 0))
top = {xy: (0, ground) for xy in ground.map}

for brick in sorted(bricks, key=lambda b: b.zlow):
    below = sorted((top[xy] for xy in brick.map), reverse=True, key=lambda zb: zb[0])
    zsupport = below[0][0]
    for support in (b for z, b in below if z == zsupport and b != ground):
        brick.supportedby.add(support)
        support.supports.add(brick)
    assert zsupport < brick.zlow
    brick.zlow = zsupport + 1
    top.update({xy: (brick.zlow + brick.height - 1, brick) for xy in brick.map})
#for y in range(ymin, ymax + 1):
#    for x in range(xmin, xmax + 1):
#        print(top[(x,y)][0], end=" ")
#    print()
#1print()

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
    print(count)
# solution: 
