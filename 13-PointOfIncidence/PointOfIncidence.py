#! /usr/bin/env python3

import aoc

args = aoc.argparse()

if args.part == 1:
    def issymetric(lines, n, before):
        after = before + 1
        if lines[before] != lines[after]:
            return False
        for l in range(min(before, n - 1 - after)):
            if lines[before - 1 - l] != lines[after + 1 + l]:
                return False
        return True

    res = 0
    for pattern in aoc.Input(groupby='paragraph'):
        rows = list(pattern)
        for up in range(len(rows) - 1):
            if issymetric(rows, len(rows), up):
                res += 100 * (up + 1)
        columns = [list(column) for column in zip(*rows)]
        for left in range(len(columns) - 1):
            if issymetric(columns, len(columns), left):
                res += left + 1
    print(res)
# solution: 29165


if args.part == 2:
    def countdiff(line1, line2):
        return  sum((1 for a, b in zip(line1, line2) if a != b))
        
    def isalmostsymetric(lines, n, before):
        after = before + 1
        count = countdiff(lines[before], lines[after])
        for l in range(min(before, n - 1 - after)):
            count += countdiff(lines[before - 1 - l], lines[after + 1 + l])
        if count == 1:
            return True
        return False

    res = 0
    for pattern in aoc.Input(groupby='paragraph'):
        rows = list(pattern)
        for up in range(len(rows) - 1):
            if isalmostsymetric(rows, len(rows), up):
                res += 100 * (up + 1)
        columns = [list(column) for column in zip(*rows)]
        for left in range(len(columns) - 1):
            if isalmostsymetric(columns, len(columns), left):
                res += left + 1
    print(res)
# solution: 32192
