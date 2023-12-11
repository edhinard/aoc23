#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    sum = 0
    for line in aoc.Input(split='', convert=int):
        digits = [x for x in line if type(x) is int]
        sum += 10 * digits[0] + digits[-1]
    print(sum)
# solution: 54561


if args.part == 2:
    spelledout = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)
    sum = 0
    for line in aoc.Input():
        digits = []
        while line:
            try:
                digit = int(line[0])
                digits.append(digit)
                line = line[1:]
                continue
            except ValueError:
                pass
            for letters, digit in spelledout.items():
                if line.startswith(letters):
                    digits.append(digit)
                    line = line[len(letters):]
                    break
            else:
                line = line[1:]
        sum += 10 * digits[0] + digits[-1]
    print(sum)
# solution: 54076
