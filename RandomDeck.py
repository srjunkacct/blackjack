from Card import *
import random


class RandomDeck:

    def draw(self):
        randomValue = int(random.uniform(0.0, 52.0))
        rank = int(randomValue / 4) + 1
        suit = randomValue % 4
        return Card(Rank(rank), Suit(suit))
