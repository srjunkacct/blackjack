
from Hand import *
from enum import Enum

class Action(Enum):
    STAND=0
    HIT=1
    DOUBLE=2
    SPLIT=3

class HandState:

    def __init__(self, hand, wasSplit, wasDoubled, done, multiplier):
        self.hand = hand
        self.wasSplit = wasSplit
        self.wasDoubled = wasDoubled
        self.multiplier = multiplier
        if self.hand.value == 21 and len(self.hand.cards) == 2:
            self.multiplier *= 1.5
        self.done = done
        self.actions = self.createActions()

    def createActions(self):
        actions=[]
        if self.done:
            return actions
        if self.hand.computeValue()[0] >= 21:
            return actions
        actions.append(Action.STAND)
        actions.append(Action.HIT)
        if ( self.hand.size() == 2):
            if self.wasDoubled == False:
                actions.append(Action.DOUBLE)
            if ( self.hand.cards[0].value() == self.hand.cards[1].value() ) and ( not ( self.wasSplit and self.hand.cards[0].value == 11 ) ):
                actions.append(Action.SPLIT)
        return actions

    def getActions(self):
        return self.actions

    def act(self, action, deck):
        if self.done == True or ( not action in self.actions ):
            raise Exception("Error:  action not valid for hand")
        if action == Action.STAND:
            return [ HandState( self.hand, self.wasSplit, self.wasDoubled, True, self.multiplier ) ]
        elif action == Action.HIT:
            hand = self.hand.hit(deck)
            return [ HandState( hand, self.wasSplit, False, False, self.multiplier ) ]
        elif action == Action.DOUBLE:
            if len(self.hand.cards) != 2:
                raise Exception("Error:  action not valid for hand")
            hand = self.hand.hit(deck)
            return [ HandState( hand, self.wasSplit, True, True, 2.0 * self.multiplier) ]
        elif action == Action.SPLIT:
            cards = self.hand.cards
            canContinue = ( cards[0].isAce() )
            oldHand = Hand( cards[0] )
            oldHand = oldHand.hit( deck )
            newHand = Hand( cards[1] )
            newHand = newHand.hit( deck )
            return ( HandState( oldHand, True, False, canContinue, self.multiplier ),
                     HandState( newHand, True, False, canContinue, self.multiplier ) )
        else:
            raise Exception("Error:  Unknown action")





