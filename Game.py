#!/usr/bin/python
from collections import deque

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
        self.playerHandStateQueue = deque()

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
            print("---------------")
            (dealerHand, playerHand ) = self.deal()
            print(" Dealer upcard is {}".format( str(dealerHand.cards[1] ) ) )
            handState = HandState(playerHand, False, False, False, 1.0)
            self.playerHandStateQueue.append( handState )
            liveHandResults = []
            while len(self.playerHandStateQueue) > 0:
                handResult = self.playHand( dealerHand, self.playerHandStateQueue.pop() )
                if handResult:
                    liveHandResults.append( handResult )

            print(" Dealer hand is {} value is {}".format( str([str(card) for card in dealerHand.cards]), dealerHand.computeRawValue()) )
            if ( len( liveHandResults) > 0 ):
                while dealerHand.computeRawValue() < 17:
                    nextCard = self.deck.draw()
                    nextCards = dealerHand.cards.copy()
                    nextCards.append(nextCard)
                    dealerHand = Hand( nextCards )
                    print(" Dealer hand is {} value is {}".format(str([str(card) for card in dealerHand.cards]),
                                                              dealerHand.computeRawValue()))
                if dealerHand.computeRawValue() > 21:
                    self.playerScore += sum( map( lambda result : result[1],
                                         filter( lambda result: result[0] <= 21, liveHandResults) ) )
                    print(" Dealer has busted.  Player score is {}".format( self.playerScore ) )
                else:
                    losingMultiplier = sum( map( lambda result : result[1],
                                         filter( lambda result: result[0] <= 21 and result[0] < dealerHand.computeRawValue(), liveHandResults) ) )
                    winningMultiplier = sum(map(lambda result: result[1],
                                           filter(lambda result: result[0] <= 21 and result[0] > dealerHand.computeRawValue(), liveHandResults)))
                    self.playerScore -= losingMultiplier
                    self.playerScore += winningMultiplier
                    print(" Player score is {}".format( self.playerScore))

    def playHand( self, dealerHand, playerHandState ):
        print(" Player hand is {} value is {}".format(str([str(card) for card in playerHandState.hand.cards]),
                                                  playerHandState.hand.computeRawValue()))
        while len(playerHandState.getActions()) > 0:
            print(" Valid player actions are {}".format(str(playerHandState.getActions())))
            print(" Enter action ( 0 = STAND, 1 = HIT, 2 = DOUBLE, 3 = SPLIT):")
            action = Action(int(input()))
            while not Action(action) in playerHandState.getActions():
                print(" Invalid action selection.  Valid player actions are {}".format(str(playerHandState.getActions())))
                print(" Enter action( 0 = STAND, 1 = HIT, 2 = DOUBLE, 3 = SPLIT):")
            playerHandState = playerHandState.act(action, self.deck)
            if ( len( playerHandState) > 1 ):
                self.playerHandStateQueue.append( playerHandState[1] )
            playerHandState = playerHandState[0]
            print(" Player hand is {} value is {}".format(str([str(card) for card in playerHandState.hand.cards]),
                                                      playerHandState.hand.computeRawValue()))
        if playerHandState.hand.computeRawValue() > 21:
            self.playerScore -= playerHandState.multiplier
            print(" Player busted.  Current player score is {}".format(self.playerScore))
            return None
        else:
            return ( playerHandState.hand.computeRawValue(), playerHandState.multiplier )

def playDealerHand( self, dealerHand, playerHandState ):
    print(" Dealer hand is {} value is {}".format(str([str(card) for card in dealerHand.cards]),
                                                  dealerHand.computeRawValue()))
    while dealerHand.computeRawValue() < 17:
        nextCard = self.deck.draw()
        nextCards = dealerHand.cards.copy()
        nextCards.append(nextCard)
        dealerHand = Hand(nextCards)
        print(" Dealer hand is {} value is {}".format(str([str(card) for card in dealerHand.cards]),
                                                      dealerHand.computeRawValue()))
    if dealerHand.computeRawValue() > 21:
        self.playerScore += playerHandState.multiplier
        print(" Dealer has busted.  Player score is {}".format(self.playerScore))
    elif dealerHand.computeRawValue() > playerHandState.hand.computeRawValue():
        self.playerScore -= playerHandState.multiplier
        print(" Dealer wins.  Player score is {}".format(self.playerScore))
    elif dealerHand.computeRawValue() < playerHandState.hand.computeRawValue():
        self.playerScore += playerHandState.multiplier
        print(" Player wins.  Player score is {}".format(self.playerScore))
    else:
        print(" Push.  Player score is {}".format(self.playerScore))
    return


if __name__ == '__main__':
    game = Game(1)
    game.play()