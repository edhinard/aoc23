#! /usr/bin/env python3

import dataclasses
import math
import re

import aoc

args = aoc.argparse()

if args.part == 1:
    map = [line for line in aoc.Input()]
    ys = 0
    xs = map[ys].find('.')
    ye = len(map) - 1
    xe = map[ye].find('.')
    longesthike = 0
    pathxys = [[(xs, ys)]]
    pathdirs = [['v']]
    while pathxys:
        print(longesthike, len(pathxys))
        pathxy = pathxys.pop(0)
        x, y =  pathxy[-1]
        pathdir = pathdirs.pop(0)
        dir = pathdir[-1]
        dx, dy = {'>': (1,0), '<':(-1,0), '^':(0,-1), 'v':(0,1)}[dir]
        nx = x + dx
        ny = y + dy
        if (nx,ny) in pathxy or nx < 0 or nx >= len(map[0]) or ny < 0 or ny>= len(map) or map[ny][nx] == '#':
            continue
        if (nx, ny) == (xe, ye):
            longesthike = max(longesthike, len(pathxy))
            continue
        if (ndir := map[ny][nx]) in '><v^':
            pathxys.append(pathxy + [(nx,ny)])
            pathdirs.append(pathdir + [ndir])
            continue
        for ndir in '><v^':
            pathxys.append(pathxy + [(nx,ny)])
            pathdirs.append(pathdir + [ndir])
    print(longesthike)
        
# solution: 2414

if args.part == 2:
    map = [line for line in aoc.Input()]
    ys = 0
    xs = map[0].find('.')
    map[0] = '#' * len(map[0])
    ye = len(map) - 1
    xe = map[ye].find('.')
    longesthike = 0
    paths = [[(xs, ys+1)]]
    while paths:
        path = paths.pop(0)
        x, y =  path[-1]
        for dx, dy in ((1,0), (-1,0), (0,-1), (0,1)):
            nx = x + dx
            ny = y + dy
            if (nx,ny) in path or map[ny][nx] == '#':
                continue
            if (nx, ny) == (xe, ye):
                longesthike = max(longesthike, 1+len(path))
                print(longesthike)
                continue
            paths.append(path + [(nx,ny)])
    print()
    print(longesthike)
# solution: 
