from game.player.player import Player
from game.map.long_john_map import LongJohnMap

class LongJohn(Player):
    
    is_free : bool
    personal_map : LongJohnMap
    bluffs : int
    hints : list

    def __init__(self):
        Player.__init__(self, "#000000")
        self.id = "longjohn"
        self.name = "Long John Silver"
        self.is_free = False
        self.personal_map = None
        self.bluffs = 0
        self.hints = []