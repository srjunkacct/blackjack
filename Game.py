#!/usr/bin/python

from Card import Card
from Deck import Deck
from Hand import Hand
class Game:

    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.deck = Deck(self.numDecks)

    def deal(self):
        dealerHole = self.deck.draw()
        dealerUp = self.deck.draw()
        dealerHand = Hand([dealerHole, dealerUp])
        player0 = self.deck.draw()
        player1 = self.deck.draw()
        playerHand = Hand([player0, player1])
        return ( dealerHand, playerHand )

    def play(self):
        cardLimit = int(13 * self.numDecks)
        while len(self.deck.cardsRemaining) > cardLimit:
            (dealerHand, playerHand ) = self.deal()
            print(" Dealer upcard is {}".format( str(dealerHand.cards[1] ) ) )
            print(" Player hand is {} value is {}".format( str([str(card) for card in playerHand.cards]), playerHand.value))

if __name__ == '__main__':
    game = Game(1)
    game.play()