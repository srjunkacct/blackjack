#!/usr/bin/python

from Card import cardFromIndex
import random

class Deck():

    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.cardsRemaining = self.shuffle()

    def shuffle(self):
        indexArray = [i for i in range(0, 52 * self.numDecks)]
        for i in range(1, 52 * self.numDecks):
            randVal = random.uniform(0,i+1)
            indexToSwapWith = int(randVal)
            tmp = indexArray[i]
            indexArray[i] = indexArray[indexToSwapWith]
            indexArray[indexToSwapWith] = tmp
        return [ cardFromIndex(i%52) for i in indexArray]

    def draw(self):
        card = self.cardsRemaining[-1]
        self.cardsRemaining = self.cardsRemaining[0:-1]
        return card








