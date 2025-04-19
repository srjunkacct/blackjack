
from HandState import Action

class RLHandState:

    def __init__(self, handState, dealerHand):
        playerValue =  handState.hand.playerValue()
        self.playerScore = playerValue[0]
        self.playerIsAceEleven = playerValue[1]
        self.dealerUpCard = dealerHand.cards[0]
        self.actions = handState.getActions()
        self.isTerminal = not any( [ action == Action.HIT for action in self.actions ] )
        self.canDouble = any( [ action == Action.DOUBLE for action in self.actions ] )
        self.canSplit = any( [ action == Action.SPLIT for action in self.actions ] )


