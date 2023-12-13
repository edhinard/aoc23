#! /usr/bin/env python3

import itertools
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
    print(num)
# solution: 7922


if args.part == 2:
    cache = dict()

    def combinations(springs, stats):
        if not springs and stats:
            return 0
        if not stats:
            if '#' in springs:
                return 0
            else:
                return 1

        if (springs, stats) in cache:
            return cache[(springs, stats)]

        comb = 0
        if springs[0] in '.?':
            comb += combinations(springs[1:], stats)

        if springs[0] in '#?':
            l = stats[0]
            if len(springs) >= l and '.' not in springs[:l] and (len(springs) == l or springs[l] != '#'):
                comb += combinations(springs[l+1:], stats[1:])

        cache[(springs, stats)] = comb
        return comb

    num = 0
    for springs, stats in aoc.Input(split=None):
        stats = tuple([int(n) for n in stats.split(',')] * 5)
        springs = '?'.join([springs] * 5)
        num += combinations(springs, stats)
    print(num)
# solution: 18093821750095
