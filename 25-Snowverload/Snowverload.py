#! /usr/bin/env python3

import functools
import operator
import random
import aoc

args = aoc.argparse()

if args.part == 1:
    def read():
        graph = {}
        for left, rights in aoc.Input(split=':'):
            for right in rights.strip().split():
                graph.setdefault(left, set()).add(right)
                graph.setdefault(right, set()).add(left)
        return graph

    graph = read()
    while True:
        while len(graph) > 2:
            u = random.choice(list(graph.keys()))
            v = random.choice(list(graph[u]))
            uv = f'{u}-{v}'
            graph[uv] = (graph.pop(u) | graph.pop(v)) - {u, v}
            for t in graph[uv]:
                graph[t].discard(u)
                graph[t].discard(v)
                graph[t].add(uv)
        a, b = graph.keys()
        graph = read()
        aneigh = functools.reduce(operator.or_, (graph[u] for u in a.split('-')))
        cuts = aneigh & set(b.split('-'))
        print(len(cuts))
        if len(cuts) == 3:
            break
    print(len(a.split('-')) * len(b.split('-')))
# solution: 589036


if args.part == 2:
    pass
# solution: 
