#! /usr/bin/env python3

import collections
import dataclasses
import math
import re
import sys

import aoc

args = aoc.argparse()


if args.part == 1:
    def handkey(item):
        hand = item[0]

        cardvalue = {card: rank for rank, card in enumerate('AKQJT98765432'[::-1])}
        handrank = 0
        kinds = collections.defaultdict(int)
        for card in hand:
            handrank = 13 * handrank + cardvalue[card]
            kinds[card] += 1
        distrib = set(kinds.values())

        if distrib == set((5,)):
            # Five of a kind
            return 6 * 13**6 + handrank
        
        if distrib == set((4, 1)):
            # Four of a kind
            return 5 * 13**6 + handrank
        
        if distrib == set((3, 2)):
            # Full house
            return 4 * 13**6 + handrank
        
        if distrib == set((3, 1)):
            # Three of a kind
            return 3 * 13**6 + handrank
        
        if len(kinds) == 3:
            # Two pair
            return 2 * 13**6 + handrank
        
        if len(kinds) == 4:
            # One pair
            return 1 * 13**6 + handrank

        # High card
        return handrank

    hands = sorted([(list(h), int(b)) for h, b in aoc.Input().iter(split=' ')], key=handkey)
    sum = 0
    for rank, (hand, bid) in enumerate(hands, start=1):
        sum += rank * bid
    print(sum)

# solution: 250120186


if args.part == 2:
    def handkey(item):
        hand = item[0]

        cardvalue = {card: rank for rank, card in enumerate('AKQT98765432J'[::-1])}
        handrank = 0
        for card in hand:
            handrank = 13 * handrank + cardvalue[card]

        # find best card
        handwithoutjokers = [card for card in hand if card != 'J']
        if not handwithoutjokers:
            hand = ['A'] * 5
        else:
            numjokers = 5 - len(handwithoutjokers)
            kinds = collections.defaultdict(int)
            for card in handwithoutjokers:
                kinds[card] += 1
            maxcount = max(kinds.values())
            bestcard = sorted([card for card in kinds if kinds[card] == maxcount], key=lambda c:cardvalue[c])[-1]
            hand = handwithoutjokers + [bestcard] * numjokers
            
        kinds = collections.defaultdict(int)
        for card in hand:
            kinds[card] += 1
        distrib = set(kinds.values())

        if distrib == set((5,)):
            # Five of a kind
            return 6 * 13**6 + handrank
        
        if distrib == set((4, 1)):
            # Four of a kind
            return 5 * 13**6 + handrank
        
        if distrib == set((3, 2)):
            # Full house
            return 4 * 13**6 + handrank
        
        if distrib == set((3, 1)):
            # Three of a kind
            return 3 * 13**6 + handrank
        
        if len(kinds) == 3:
            # Two pair
            return 2 * 13**6 + handrank
        
        if len(kinds) == 4:
            # One pair
            return 1 * 13**6 + handrank

        # High card
        return handrank

    hands = sorted([(list(h), int(b)) for h, b in aoc.Input().iter(split=' ')], key=handkey)
    sum = 0
    for rank, (hand, bid) in enumerate(hands, start=1):
        sum += rank * bid
    print(sum)

# solution: 250665248
