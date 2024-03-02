import unittest

from Deck import Deck
class MyTestCase(unittest.TestCase):
    def test_something(self):
        deck = Deck(2)
        self.assertEqual(104, len(deck.cardsRemaining))


if __name__ == '__main__':
    unittest.main()
