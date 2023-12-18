#! /usr/bin/env python3

import collections

import aoc

args = aoc.argparse()

# It is asked to sort the hands. For that the sorted() function is used with its key=function argument.
# Parts 1 and 2 have their own key function. The key function is given a hand (and a unused bid) and returns
# the sum of
#  - a combination value: from 6 (Five of a kind) to 0 (High card)
#  - a hand value (very simplified compared to poker rules) which equivalent to a base-13 encoding
# the combination value is multiplied by 13**6 (greater than every hand value in order to give precedence on it)


# Combinations differs by the number of identical cards
def combinationvalue(hand):
    kinds = collections.defaultdict(int)
    for card in hand:
        kinds[card] += 1
    distrib = set(kinds.values())

    if distrib == set((5,)):
        # Five of a kind
        return 6

    if distrib == set((4, 1)):
        # Four of a kind
        return 5

    if distrib == set((3, 2)):
        # Full house
        return 4

    if distrib == set((3, 1)):
        # Three of a kind
        return 3

    if len(kinds) == 3:
        # Two pair
        return 2

    if len(kinds) == 4:
        # One pair
        return 1

    # High card
    return 0


# No surprise for part 1 when J is a JACK
def handkeynojokers(item):
    hand, unusedbid = item

    cardvalue = {card: rank for rank, card in enumerate('AKQJT98765432'[::-1])}
    handvalue = 0
    for card in hand:
        handvalue = 13 * handvalue + cardvalue[card]

    return combinationvalue(hand) * 13**6 + handvalue

# In part 2, J is a Joker
def handkeywithjokers(item):
    hand, unusedbid = item

    cardvalue = {card: rank for rank, card in enumerate('AKQT98765432J'[::-1])}
    handvalue = 0
    for card in hand:
        handvalue = 13 * handvalue + cardvalue[card]

    # find the best card
    nojokers = [card for card in hand if card != 'J']
    if not nojokers:
        bestcard = 'A'
    else:
        kinds = collections.defaultdict(int)
        for card in nojokers:
            kinds[card] += 1
        maxcount = max(kinds.values())
        bestcard = sorted([card for card in kinds if kinds[card] == maxcount], key=lambda c: cardvalue[c])[-1]

    # replace J by bestcard
    hand = ''.join(c if c != 'J' else bestcard for c in hand)

    return combinationvalue(hand) * 13**6 + handvalue


if args.part == 1:
    handkey = handkeynojokers
# solution: 250120186

if args.part == 2:
    handkey = handkeywithjokers
# solution: 250665248



# Sort the hands (one hand per line)
hands = sorted(list(aoc.Input(split=None)), key=handkey)

# And then sum the product of the bid and the rank
sum = 0
for rank, (hand, bid) in enumerate(hands, start=1):
    sum += rank * int(bid)
print(sum)
