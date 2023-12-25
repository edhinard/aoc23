#! /usr/bin/env python3

import dataclasses
import math
import re

import aoc

args = aoc.argparse()

if args.part == 1:
    xmin = ymin = 7 if aoc.TEST else 200000000000000
    xmax = ymax = 27 if aoc.TEST else 400000000000000

    stones= []
    for p, v in aoc.Input(split='@'):
        px,py,pz = map(int, p.split(','))
        vx,vy,vz = map(int, v.split(','))
        stones.append((px,py,vx,vy))


    count = 0
    for i, (px1, py1, vx1, vy1) in enumerate(stones[:-1]):
        for px2, py2, vx2, vy2 in stones[i+1:]:
            det = (vx2 * vy1) - (vx1 * vy2)
            if det == 0:
                continue
            k1 = (-vy2 * (px2 - px1) + vx2 * (py2 - py1)) / det
            k2 = (-vy1 * (px2 - px1) + vx1 * (py2 - py1)) / det
            if k1 < 0 or k2 < 0:
                continue
            x = px1 + k1 * vx1
            y = py1 + k1 * vy1
            if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
                count += 1
    print(count)
# solution: 18184


if args.part == 2:
    stones= []
    for p, v in aoc.Input(split='@'):
        px,py,pz = map(int, p.split(','))
        vx,vy,vz = map(int, v.split(','))
        stones.append((px,py,pz,vx,vy,vz))

    for i, (px1, py1, pz1, vx1, vy1, vz1) in enumerate(stones[:-1]):
        for j, (px2, py2, pz2, vx2, vy2, vz2) in enumerate(stones[i+1:], start=i+1):
            if vx1 * vx2 * vy1 * vy2 * vz1 * vz2:
                if vx1 / vx2 == vy1 / vy2 and vy1 / vy2 == vz1 / vz2:
                    print(i,j)
            else:
                print(vx1,vy1,vz1,vx2,vy2,vz2)
        
        # solution: 
