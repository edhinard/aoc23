#! /usr/bin/env python3

import aoc
import dataclasses

args = aoc.argparse()


if args.part == 1:
    sum = 0
    for line in aoc.Input():
        # split line at colon
        # extract card number from the left part
        # keep the right part (the list of numbers)
        # split the right part at pipe to get winning and effective numbers
        card, numbers = line.split(':')
        num = int(card.split()[1])
        winning, effective = (set(num.split()) for num in numbers.split('|'))

        # compute length of union of the two sets and the card value which is accumulated
        nummatches = len(winning & effective)
        if nummatches:
            sum += 2 ** (nummatches - 1)
    print(sum)
# solution: 21558


if args.part == 2:
    @dataclasses.dataclass
    class Card:
        macthingnumbers: int
        number: int = 1

    cards = []
    for line in aoc.Input():
        # split line at colon
        # extract card number from the left part
        # keep the right part (the list of numbers)
        # split the right part at pipe to get winning and effective numbers
        card, numbers = line.split(':')
        num = int(card.split()[1])
        winning, effective = (set(num.split()) for num in numbers.split('|'))

        # compute length of union of the two sets
        # store the number of match of each
        cards.append(Card(len(winning & effective)))

    # update the number of cards:
    #  every n macthingnumbers of a card increment by one the number of the n next cards
    for cardindex, card in enumerate(cards):
        for i in range(card.macthingnumbers):
            cards[cardindex + i + 1].number += card.number

    # The total number of cards
    print(sum(card.number for card in cards))
# solution: 10425665
