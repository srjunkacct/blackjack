#!/usr/bin/python

from Card import Card
from Deck import Deck
from Hand import Hand
from HandState import HandState, Action
from RandomDeck import RandomDeck

class Game:

    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.deck = RandomDeck()
        self.playerScore = 0.0

    def deal(self):
        dealerHole = self.deck.draw()
        dealerUp = self.deck.draw()
        dealerHand = Hand([dealerHole, dealerUp])
        player0 = self.deck.draw()
        player1 = self.deck.draw()
        playerHand = Hand([player0, player1])
        return ( dealerHand, playerHand )

    def play(self):
        while True:
            (dealerHand, playerHand ) = self.deal()
            print(" Dealer upcard is {}".format( str(dealerHand.cards[1] ) ) )
            handState = HandState(playerHand, False, False, False, 1.0)
            print(" Player hand is {} value is {}".format( str([str(card) for card in playerHand.cards]), handState.hand.computeRawValue()))
            while len( handState.getActions() ) > 0:
                print(" Valid player actions are {}".format(str(handState.getActions() ) ) )
                print(" Enter action ( 0 = STAND, 1 = HIT, 2 = DOUBLE, 3 = SPLIT):")
                action = Action(int(input()))
                while not Action(action) in handState.getActions():
                    print(" Invalid action selection.  Valid player actions are {}".format(str(handState.getActions())))
                    print(" Enter action( 0 = STAND, 1 = HIT, 2 = DOUBLE, 3 = SPLIT):")
                handState = handState.act( action, self.deck )
                print(" Player hand is {} value is {}".format(str([str(card) for card in handState.hand.cards]), handState.hand.computeRawValue()))
            if handState.hand.computeRawValue() > 21:
                self.playerScore -= handState.multiplier
                print(" Player busted.  Current plaer score is {}".format( self.playerScore))
                continue
            print(" Dealer hand is {} value is {}".format( str([str(card) for card in dealerHand.cards]), dealerHand.computeRawValue()) )
            while dealerHand.computeRawValue() < 17:
                nextCard = self.deck.draw()
                nextCards = dealerHand.cards.copy()
                nextCards.append(nextCard)
                dealerHand = Hand( nextCards )
                print(" Dealer hand is {} value is {}".format(str([str(card) for card in dealerHand.cards]),
                                                              dealerHand.computeRawValue()))
            if dealerHand.computeRawValue() > 21:
                self.playerScore += handState.multiplier
                print(" Dealer has busted.  Player score is {}".format( self.playerScore ) )
            elif dealerHand.computeRawValue() > handState.hand.computeRawValue():
                self.playerScore -= handState.multiplier
                print(" Dealer wins.  Player score is {}".format( self.playerScore))
            elif dealerHand.computeRawValue() < handState.hand.computeRawValue():
                self.playerScore += handState.multiplier
                print(" Player wins.  Player score is {}".format( self.playerScore))
            else:
                print(" Push.  Player score is {}".format( self.playerScore))
        return


if __name__ == '__main__':
    game = Game(1)
    game.play()