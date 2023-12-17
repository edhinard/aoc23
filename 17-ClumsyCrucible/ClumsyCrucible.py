#! /usr/bin/env python3

import bisect
import math
import aoc

args = aoc.argparse()

if args.part == 1:
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    
    map = [line for line in aoc.Input(split='', convert=int)]
    xmax = len(map[0])
    ymax = len(map)
    distancemax = (xmax - 1) + (ymax - 1)
    loss = 0
    stack = [(distancemax, loss, DOWN, 0, 0), (distancemax, loss, RIGHT, 0, 0)]
    seen = {(0,0,'-'): 0, (0,0,'|'): 0}
    minloss = math.inf
    minloss = 650
    while stack:
        distance, loss, dir, X, Y = stack.pop(0)
        #print(len(stack), len(seen), minloss, (distance, loss, dir, X, Y))
        if X == xmax - 1 and Y == ymax - 1:
            minloss = min(minloss, loss)
            continue
        if dir == RIGHT:
            if seen.get((X,Y,'-')) < loss:
                continue
            states = []
            for _ in range(3):
                X += 1
                if X == xmax:
                    break
                distance -= 1
                loss += map[Y][X]
                localminloss = seen.setdefault((X, Y, '|'), math.inf)
                if loss < localminloss and loss < minloss:
                    state1 = (distance, loss, DOWN, X, Y)
                    state2 = (distance, loss, UP, X, Y)
                    i = bisect.bisect(stack, state1)
                    stack.insert(i, state2)
                    stack.insert(i, state1)
                    seen[(X, Y, '|')] = loss

        elif dir == LEFT:
            if seen.get((X,Y,'-')) < loss:
                continue
            for _ in range(3):
                X -= 1
                if X == -1:
                    break
                distance += 1
                loss += map[Y][X]
                localminloss = seen.setdefault((X, Y, '|'), math.inf)
                if loss < localminloss and loss < minloss:
                    state1 = (distance, loss, DOWN, X, Y)
                    state2 = (distance, loss, UP, X, Y)
                    i = bisect.bisect(stack, state1)
                    stack.insert(i, state2)
                    stack.insert(i, state1)
                    seen[(X, Y, '|')] = loss

        elif dir == UP:
            if seen.get((X,Y,'|')) < loss:
                continue
            for _ in range(3):
                Y -= 1
                if Y == -1:
                    break
                distance += 1
                loss += map[Y][X]
                localminloss = seen.setdefault((X, Y, '-'), math.inf)
                if loss < localminloss and loss < minloss:
                    state1 = (distance, loss, RIGHT, X, Y)
                    state2 = (distance, loss, LEFT, X, Y)
                    i = bisect.bisect(stack, state1)
                    stack.insert(i, state2)
                    stack.insert(i, state1)
                    seen[(X, Y, '-')] = loss

        elif dir == DOWN:
            if seen.get((X,Y,'|')) < loss:
                continue
            for _ in range(3):
                Y += 1
                if Y == ymax:
                    break
                distance -= 1
                loss += map[Y][X]
                localminloss = seen.setdefault((X, Y, '-'), math.inf)
                if loss < localminloss and loss < minloss:
                    state1 = (distance, loss, RIGHT, X, Y)
                    state2 = (distance, loss, LEFT, X, Y)
                    i = bisect.bisect(stack, state1)
                    stack.insert(i, state2)
                    stack.insert(i, state1)
                    seen[(X, Y, '-')] = loss
    print(minloss)
# solution: 638


if args.part == 2:
    pass
# solution: 
