import unittest
from Card import *
from HandState import *



class HandStateTest(unittest.TestCase):
    def testActions(self):
        hand = Hand( [Card( Rank.TEN, Suit.SPADES), Card(Rank.TEN, Suit.DIAMONDS) ] )
        handState = HandState( hand, False, False, 1)
        self.assertEqual([Action.STAND, Action.HIT, Action.DOUBLE, Action.SPLIT], handState.getActions())
        hand = Hand( [Card( Rank.TEN, Suit.SPADES), Card(Rank.NINE, Suit.DIAMONDS)])
        handState = HandState(hand, False, False, 1)
        self.assertEqual([Action.STAND, Action.HIT, Action.DOUBLE], handState.getActions() )
        hand = Hand( [Card( Rank.TEN, Suit.SPADES), Card( Rank.TWO, Suit.SPADES), Card( Rank.THREE, Suit.SPADES)])
        handState = HandState( hand, False, True, 2 )
        self.assertEqual([Action.STAND, Action.HIT], handState.getActions())


if __name__ == '__main__':
    unittest.main()
