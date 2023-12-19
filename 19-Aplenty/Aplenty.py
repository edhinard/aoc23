#! /usr/bin/env python3

import functools
import operator
import re

import aoc

args = aoc.argparse()

# Read first paragraph of input which is the worfflow definitions
# Workflows are stored by name. Each contains a list of rules and a default workflowname
# Rules are 4-uplets with: key (x, m, a or s), comparison (< or >), value (integer) and workflowname
input = aoc.Input(groupby='paragraph')
workflows = dict()
input.split = re.compile(r'([^{]+){([^}]+)}')
for name, rulestr in next(input):
    rules = [rule for rule in rulestr.split(',')]
    default = rules.pop()
    def mkrul(rule):
        cond, wname = rule.split(':')
        return ((*cond.partition('<'), wname) if '<' in cond else (*cond.partition('>'), wname))
    rules = [mkrul(rule) for rule in rules]
    workflows[name] = (rules, default)


if args.part == 1:
    # For each part (in second paragraph of input) decoded as a dict
    #  follow the workflow rules (starting with 'in') until 'A' or 'R' is reached
    input.split = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    input.convert = int
    count = 0
    for part in (dict(x=x, m=m, a=a, s=s) for x, m, a, s in next(input)):
        workflowname = 'in'
        while workflowname not in ('A', 'R'):
            rules, default = workflows[workflowname]
            for key, comp, val, wname in rules:
                if comp == '>' and part[key] > int(val):
                    workflowname = wname
                    break
                if comp == '<' and part[key] < int(val):
                    workflowname = wname
                    break
            else:
                workflowname = default

        # Only if ended up in 'A': accumulate the part values
        if workflowname == 'A':
            count += sum(part.values())

    print(count)
# solution: 402185


if args.part == 2:
    # Here, the second paragraph of input is not used
    # Instead, the workflow graph is fully traversed and each path that
    # ends with the acceptance of the part is retained with its list of
    # conditions
    acceptancepaths = []
    states = [('in', [])]
    while states:
        workflowname, conditions = states.pop(0)
        if workflowname == 'A':
            acceptancepaths.append(conditions)
        elif workflowname != 'R':
            rules, default = workflows[workflowname]
            for key, comp, val, wname in rules:
                # new state with the conditions list extended
                states.append((wname, conditions + [(key, comp, val)]))

                # extend conditions list with the inverse condition
                comp = {'>': '<=', '<=': '>', '<': '>=', '>=': '<'}[comp]
                conditions.append((key, comp, val))

            # a last state with the default
            states.append((default, conditions))

    # Count the number of combination for each acceptance path
    count = 0
    for conditions in acceptancepaths:
        # The starting ranges of each rating is [1, 4000]
        # those ranges are limited by the lower or upper bounds accorded to the conditions
        # that we want to satisfy
        ranges = dict(x=[1,4000], m=[1,4000], a=[1,4000], s=[1,4000])
        for key, comp, val in conditions:
            if comp == '>':
                ranges[key][0] = int(val) + 1
            elif comp == '>=':
                ranges[key][0] = int(val)
            elif comp == '<=':
                ranges[key][1] = int(val)
            elif comp == '<':
                ranges[key][1] = int(val) - 1

        # The number of combinations for an acceptance path is the product of the range lengths
        count += functools.reduce(operator.mul, [b - a + 1 for a, b in ranges.values()], 1)

    print(count)
# solution: 130291480568730
