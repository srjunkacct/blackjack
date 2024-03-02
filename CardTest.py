import unittest

from Card import Suit, Rank, Card, cardFromIndex, singleDeck

class MyTestCase(unittest.TestCase):
    def test_something(self):
        deck = singleDeck()
        card = deck[3]
        self.assertEqual(Rank.ACE, card.rank)
        self.assertEqual(Suit.SPADES, card.suit)


if __name__ == '__main__':
    unittest.main()
