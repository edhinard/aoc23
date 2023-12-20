#! /usr/bin/env python3

import dataclasses
import math
import re

import aoc
args = aoc.argparse()



@dataclasses.dataclass
class Flipflop:
    dst: []
    state: int = 0

    def trig(self, src, pulse):
        if pulse:
            return
        self.state = 1 - self.state
        for name in self.dst:
            yield name, self.state

@dataclasses.dataclass
class Conjunction:
    dst: []
    state: dict = dataclasses.field(default_factory=dict)

    def trig(self, src, pulse):
        self.state[src] = pulse
        out = 0 if sum(self.state.values()) == len(self.state) else 1
        for name in self.dst:
            yield name, out

modules = dict()
for src, dst in aoc.Input(split=' -> '):
    dst = [d.strip() for d in dst.split(',')]
    if src[0] == '%':
        modules[src[1:]] = Flipflop(dst)
    elif src[0] == '&':
        modules[src[1:]] = Conjunction(dst)
    elif src == 'broadcaster':
        broadcaster = dst

for name, module in modules.items():
    for m in module.dst:
        if m not in modules:
            hole = m
        elif isinstance(modules[m], Conjunction):
            modules[m].state[name] = 0

if args.part == 1:               
    count = {0: 0, 1: 0}
    for _ in range(1000):
        count[0] += 1
        states = [('broadcaster', 0, dst) for dst in broadcaster]
        while states:
            currentstates = states
            states = []
            for src, pulse, dst in currentstates:
                #print(f"{src} -{pulse}-> {dst}")
                count[pulse] += 1
                if dst == hole:
                    continue
                module = modules[dst]
                states.extend(((dst, p, n) for n, p in module.trig(src, pulse)))
    print(count[0] * count[1])
# solution: 


if args.part == 2:
    press = 0
    while True:
        press += 1
        if press % 10000 == 0:
            print(press)
        states = [('broadcaster', 0, dst) for dst in broadcaster]
        while states:
            currentstates = states
            states = []
            for src, pulse, dst in currentstates:
                #print(f"{src} -{pulse}-> {dst}")
                if dst == hole:
                    if not pulse:
                        break
                    else:
                        continue
                module = modules[dst]
                states.extend(((dst, p, n) for n, p in module.trig(src, pulse)))
    print(press)
# solution: 
