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

    visited = set()
    graph = {(xs, ys): [], (xe, ye): []}
    states = [[(xs, ys), (xs, ys + 1)]]
    while states:
        edge = states[0]
        x, y =  edge[-1]
        if (x, y) in graph:
            states.pop(0)
            graph[edge[0]].append(((x, y), len(edge) - 1))
            graph[(x, y)].append((edge[0], len(edge) - 1))
            continue
        nextcells = []
        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy
            if (nx,ny) in edge or map[ny][nx] == '#' or (x, y) in visited:
                continue
            nextcells.append((nx, ny))
        if len(nextcells) == 0:
            states.pop(0)
            continue
        if len(nextcells) == 1:
            visited.add((x, y))
            edge.append(nextcells[0])
        else:
            states.pop(0)
            states.extend(([(x, y) , nextcell] for nextcell in nextcells))
            graph[edge[0]].append((edge[-1], len(edge) - 1))
            graph[(x, y)] = [(edge[0], len(edge) - 1)]

    beforeend, lastlength = graph[(xe, ye)][0]
    longest = 0
    states = [[[(xs, ys)], 0]]
    while states:
        path, length = states.pop(0)
        if path[-1] == beforeend:
            longest = max(longest, length + lastlength)
            print(longest, len(states))
            continue
        for v, l in graph[path[-1]]:
            if v not in path:
                states.append((path + [v], length + l))
    
        
    print(longest)
# solution: 6598 in many hours

