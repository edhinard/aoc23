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
         #       if abs(X+Y+x+y)%2==steps%2 and (x, y) in state:
        #            print("O", end="")
        #            assert map[y][x] in 'S.'
        #        else:
        #            print(map[y][x], end="")
        #    print()
                        
        return sum((int(abs(X-x+Y-y)%2==steps%2) for x,y in state))

    print(plots(65, 65, 500))
    print(a:=plots(0, 0, 64))
    print(b:=plots(0, 130, 64))
    print(c:=plots(130, 0, 64))
    print(d:=plots(130, 130, 64))
    print(e:=plots(65, 65, 64))
    print(a+b+c+d+e)
    print()
    print(plots(65, 65, 499))
    print(a:=plots(0, 0, 63))
    print(b:=plots(0, 130, 63))
    print(c:=plots(130, 0, 63))
    print(d:=plots(130, 130, 63))
    print(e:=plots(65, 65, 63))
    print(a+b+c+d+e)
          
    #surf = ((2 * steps - 1) ** 2) / 2
    #num = surf / (131 ** 2)
    #print(surf, num, num * count)

    # 1206401570982281
    # 602586903152965
    #map = [line for line in aoc.Input()]
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
