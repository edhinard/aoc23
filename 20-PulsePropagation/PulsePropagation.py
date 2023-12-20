#! /usr/bin/env python3

import dataclasses
import functools
import operator

import aoc
args = aoc.argparse()


@dataclasses.dataclass
class Flipflop:
    dst: []
    state: int = 0

    # This module get triggered by src with a pulse (0=Low/1=High)
    # output tuples of (destination module, pulse (0/1))
    # where to propagate pulses
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

    # Same method as Flipflop, different behaviour
    def trig(self, src, pulse):
        self.state[src] = pulse
        out = 0 if sum(self.state.values()) == len(self.state) else 1
        for name in self.dst:
            yield name, out


# Store modules by name. Each module is one of the two above class
#  with their behaviour coded in the trig() function
# For broadcaster store destination
# Locate hole
modules = dict()
for src, dst in aoc.Input(split=' -> '):
    dst = [d.strip() for d in dst.split(',')]
    if src[0] == '%':
        modules[src[1:]] = Flipflop(dst)
    elif src[0] == '&':
        modules[src[1:]] = Conjunction(dst)
    elif src == 'broadcaster':
        broadcaster = dst

# Initialize module states
for name, module in modules.items():
    for m in module.dst:
        if m not in modules:
            hole = m
        elif isinstance(modules[m], Conjunction):
            modules[m].state[name] = 0

if args.part == 1:
    def press(count):
        global broadcaster, modules, hole

        count[0] += 1
        states = [('broadcaster', 0, dst) for dst in broadcaster]
        while states:
            currentstates = states
            states = []
            for src, pulse, dst in currentstates:
                # print(f"{src} -{pulse}-> {dst}")
                count[pulse] += 1
                if dst == hole:
                    continue
                module = modules[dst]
                states.extend(((dst, p, n) for n, p in module.trig(src, pulse)))

    count = {0: 0, 1: 0}
    for _ in range(1000):
        press(count)
    print(count[0] * count[1])
# solution: 861743850


if args.part == 2:
    # Analyzing the input file here is what look like the end of the connection graph:
    #     dh mk
    #      | |
    #      v v
    # vf-> &jz <-rn
    #       |
    #       v
    #       rx
    # The rx module will receive it's first Low pulse when the modules vf, dh, mk and rn
    #  will send a High one.
    # It has been observed that all those modules have a peridodic output that looks like:
    #    0,0,...,0,1
    # The result should be a multiple of the product of the period. The product matches. Stop.
    assert hole == 'rx'
    lastmodule = [name for name, module in modules.items() if hole in module.dst][0]
    modulestowatch = {name: 0 for name, module in modules.items() if lastmodule in module.dst}

    def press(modulestowatch):
        global broadcaster, modules, hole

        highpulsed = None
        states = [('broadcaster', 0, dst) for dst in broadcaster]
        while states:
            currentstates = states
            states = []
            for src, pulse, dst in currentstates:
                # print(f"{src} -{pulse}-> {dst}")
                if dst == hole:
                    continue
                if src in modulestowatch and pulse:
                    highpulsed = src
                module = modules[dst]
                states.extend(((dst, p, n) for n, p in module.trig(src, pulse)))
        return highpulsed

    count = 0
    while (res := functools.reduce(operator.mul, modulestowatch.values(), 1)) == 0:
        count += 1
        if m := press(modulestowatch.keys()):
            modulestowatch[m] = count
            print(modulestowatch)
    print(res)
# solution: 247023644760071
