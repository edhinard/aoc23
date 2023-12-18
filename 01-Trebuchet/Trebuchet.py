#! /usr/bin/env python3

import aoc

args = aoc.argparse()


if args.part == 1:
    sum = 0
    for line in aoc.Input(split='', convert=int):
        # line is already splitted, and item converted to int if possible
        digits = [x for x in line if type(x) is int]

        # calibration value combines the first digit and the last digit
        sum += 10 * digits[0] + digits[-1]

    print(sum)
# solution: 54561


if args.part == 2:
    sum = 0
    for line in aoc.Input():
        digits = []
        while line:
            # First option: the first char of line is a digit
            #  - append this digit to the list and
            #  - truncate the line by one on the left
            try:
                digits.append(int(line[0]))
                line = line[1:]
                continue
            except ValueError:
                pass

            # Second option: the first char of line is a letter
            #  find which of the spelled out digit can starts the line
            #   - append this digit to the list and
            #   - truncate the line by the length of the word on the left
            #  or if no spelled out digit is found
            #   - truncate line string by one on the left
            for digit, letters in enumerate("one two three four five six seven eight nine".split(), start=1):
                if line.startswith(letters):
                    digits.append(digit)
                    line = line[len(letters):]
                    break
            else:
                line = line[1:]

        # calibration value combines the first digit and the last digit
        sum += 10 * digits[0] + digits[-1]

    print(sum)
# solution: 54076
