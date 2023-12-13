#! /usr/bin/env python3

import itertools
import math
import re

import aoc

args = aoc.argparse()

if args.part == 1:
    def damaged(springs):
        springs = list(springs)
        groups = []
        currentsize = 0
        while springs:
            spring = springs.pop(0)
            if spring == '#':
                currentsize += 1
            elif currentsize:
                groups.append(currentsize)
                currentsize = 0
        if currentsize:
            groups.append(currentsize)
        return groups

    def possiblesprings(springs, numnewdamaged):
        unk = [pos for pos, spring in enumerate(springs) if spring == '?']
        for comb in itertools.combinations(list(range(len(unk))), numnewdamaged):
            newsprings = list(springs.replace('?', '.'))
            for pos in comb:
                newsprings[unk[pos]] = '#'
            yield ''.join(newsprings)

    num = 0
    for springs, stats in aoc.Input(split=None):
        stats = [int(n) for n in stats.split(',')]
        numnewdamaged = sum(stats) - sum((1 for spring in springs if spring == '#'))
        num += sum(1 for onesprings in possiblesprings(springs, numnewdamaged) if damaged(onesprings) == stats)
        #print("="*50)
        #print(springs, stats)
        #for onesprings in possiblesprings(springs, numnewdamaged):
        #    print(onesprings, damaged(onesprings))
        #print(sum(1 for onesprings in possiblesprings(springs, numnewdamaged) if damaged(onesprings) == stats))
        #print()
    #print()
    print(num)
# solution: 


if args.part == 2:
    pass
# solution: 
