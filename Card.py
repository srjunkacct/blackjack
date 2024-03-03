#!/usr/bin/python

from enum import Enum

class Suit(Enum):
    CLUBS=0
    DIAMONDS=1
    HEARTS=2
    SPADES=3

class Rank(Enum):
    ACE=1
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5
    SIX=6
    SEVEN=7
    EIGHT=8
    NINE=9
    TEN=10
    JACK=11
    QUEEN=12
    KING=13

def cardFromIndex(index):
    suitIndex = index % 4
    rankIndex = 1 + int(index / 4)
    return Card(Rank(rankIndex), Suit(suitIndex))

def singleDeck():
    return [cardFromIndex(index) for index in range(0,52)]

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def value(self):
        if self.rank.name == 'ACE':
            return 1
        if self.rank.name == 'TWO':
            return 2
        if self.rank.name == 'THREE':
            return 3
        if self.rank.name == 'FOUR':
            return 4
        if self.rank.name == 'FIVE':
            return 5
        if self.rank.name == 'SIX':
            return 6
        if self.rank.name == 'SEVEN':
            return 7
        if self.rank.name == 'EIGHT':
            return 8
        if self.rank.name == 'NINE':
            return 9
        return 10

    def isAce(self):
        return self.rank.name == 'ACE'


