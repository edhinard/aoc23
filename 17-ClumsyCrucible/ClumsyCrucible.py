#! /usr/bin/env python3

import heapq
import aoc

args = aoc.argparse()

if args.part == 1:
    minlen = 1
    maxlen = 3
# solution: 638


if args.part == 2:
    minlen = 4
    maxlen = 10
# solution: 748


DOWN = 0
RIGHT = 1
UP = 2
LEFT = 3

map = [line for line in aoc.Input(split='', convert=int)]
xmax = len(map[0])
ymax = len(map)
queue = [(0, DOWN, 0, 0), (0, RIGHT, 0, 0)]
seen = set()

# Dijkstra's algorithm to find the minimum loss path to destination
# Nodes of the graph are blocks at which direction changes. Module heapq is used
# to always process the node with the minimum loss
# The seen set is there to avoid looping
# Once the destination block is reached we know for sure it is with the minimum loss
while queue:
    loss, direction, x, y = heapq.heappop(queue)
    if x == xmax - 1 and y == ymax - 1:
        break

    dx, dy, dir1, dir2 = {
        DOWN: (0, 1, RIGHT, LEFT),
        RIGHT: (1, 0, DOWN, UP),
        UP: (0, -1, RIGHT, LEFT),
        LEFT: (-1, 0, DOWN, UP)}[direction]

    prevx, prevy = x, y
    for _ in range(maxlen):
        x += dx
        y += dy
        if x < 0 or x >= xmax or y < 0 or y >= ymax:
            break
        loss += map[y][x]
        if _ < minlen - 1:
            continue
        if (prevx, prevy, x, y) not in seen:
            seen.add((prevx, prevy, x, y))
            heapq.heappush(queue, (loss, dir1, x, y))
            heapq.heappush(queue, (loss, dir2, x, y))

print(loss)
