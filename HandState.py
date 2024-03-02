
from enun import Enum

class Action(Enum):
    STAND=0
    HIT=1
    DOUBLE=2
    SPLIT=3
    


class HandState:

    def __init__(self, hand, wasSplit):
        self.hand = hand
        self.wasSplit = wasSplit
        self.actions = actions