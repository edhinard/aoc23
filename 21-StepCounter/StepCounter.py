#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    steps = 64
    map = [line for line in aoc.Input()]
    for Y, line in enumerate(map):
        if 'S' in line:
            X = line.index('S')
            break

    state = set([(X,Y)])
    for _ in range(steps):
        for x,y in list(state):
            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                nx = x + dx
                ny = y + dy
                if map[ny][nx] != '#':
                    state.add((nx, ny))
    count = sum(( int(abs(X+Y+x+y)%2==steps%2) for x,y in state))
    print(count)

    #for y in range(len(map)):
    #    for x in range(len(map[0])):
    #        if abs(X+Y+x+y)%2==steps%2 and (x, y) in state:
    #            print("O", end="")
    #            assert map[y][x] in 'S.'
    #        else:
    #            print(map[y][x], end="")
    #    print()

    
# solution: 3615


if args.part == 2:
    steps = 26501365
    #5 * 11 * 481843
    
    map = [line for line in aoc.Input()]
    plots = sum((line.count('.') for line in aoc.Input())) + 1
    print(plots)
    #maps = [
    #    [''.join(reversed(line[:65+1])) for line in reversed(map[:65+1])],
    #    [line[65:] for line in reversed(map[:65+1])],
    #    [''.join(reversed(line[:65+1])) for line in map[65:]],
    #    [line[65:] for line in map[65:]]
    #]
    #for m in maps:
    #    print('\n'.join(m))
    #    print()

    
# solution: 
