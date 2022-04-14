from game.map import LongJohnMap
from game.player.Player import Player


class LongJohn(Player):

    def __init__(self):
        Player.__init__(self, "#000000")