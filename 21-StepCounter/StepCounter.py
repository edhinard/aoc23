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
    count = sum((int(abs(X+Y+x+y)%2==steps%2) for x,y in state))
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

    map = [line for line in aoc.Input()]
    for Y, line in enumerate(map):
        if 'S' in line:
            X = line.index('S')
            map[Y] = line.replace('S', '.')
            break

    def plots(X, Y, steps):
        global map
        state = set([(X, Y)])
        for _ in range(steps):
            for x,y in list(state):
                for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < len(map[0]) and ny >= 0 and ny < len(map) and map[ny][nx] != '#':
                        state.add((nx, ny))
        #for y in range(len(map)):
        #    for x in range(len(map[0])):
        #        if abs(X+Y+x+y)%2==steps%2 and (x, y) in state:
        #            print("O", end="")
        #            assert map[y][x] in 'S.'
        #        else:
        #            print(map[y][x], end="")
        #    print()                        
        return sum((int(abs(X-x+Y-y)%2==steps%2) for x,y in state))

    
    n = (steps - 130) // 131
    assert steps%2 == 1
    assert n%2 == 1
    
    fartherdistanceinfull = 130 + n * 131
    border = ((n + 1) * (plots(0, 0, steps - (fartherdistanceinfull + 2)) +
                         plots(130, 0, steps - (fartherdistanceinfull + 2)) +
                         plots(0, 130, steps - (fartherdistanceinfull + 2)) +
                         plots(130, 130, steps - (fartherdistanceinfull + 2))) +
              n * (plots(0, 0,  steps - (fartherdistanceinfull - 131 + 2)) +
                   plots(130, 0,  steps - (fartherdistanceinfull - 131 + 2)) +
                   plots(0, 130,  steps - (fartherdistanceinfull - 131 + 2)) +
                   plots(130, 130,  steps - (fartherdistanceinfull - 131 + 2))))

    vertices = (plots(0, 65, steps - (fartherdistanceinfull - 65 + 1)) +
                plots(130, 65, steps - (fartherdistanceinfull - 65 + 1)) +
                plots(65, 0, steps - (fartherdistanceinfull - 65 + 1)) +
                plots(65, 130, steps - (fartherdistanceinfull - 65 + 1)))
    
    fullodd = plots(65, 65, 129)
    fulleven = plots(65, 65, 130)
    inside = ((n + 1) ** 2) * fulleven + (1 + (n - 1) * (n + 1)) * fullodd

    print(inside + border + vertices)
# solution: 602259568764234
