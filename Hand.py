#!/usr/bin/python

from Card import Card
from Deck import Deck


# Value is a 2-tuple ( score, isthereanAceCountedAs11 ).
class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.value = self.computeValue()

    def __str__(self):
        return str(self.cards)

    def computeRawValue(self):
        return self.computeValue()[0]

    def computeValue(self):
        score = sum([card.value() for card in self.cards])
        hasAce = any([card.isAce() for card in self.cards])
        if hasAce and score <= 11:
            return (score + 10, True)
        return (score, False)

    def isBlackjack(self):
        return self.computeValue() == 21 and len(self.cards) == 2

    def hit(self, deck):
        drawnCard = deck.draw()
        newCards = self.cards.copy()
        newCards.append(drawnCard)
        return Hand(newCards)

    def size(self):
        return len(self.cards)

