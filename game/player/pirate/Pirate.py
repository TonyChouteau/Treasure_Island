from game.player.Player import Player


class Pirate(Player):

    def __init__(self, color):
        Player.__init__(self, color)
        self.interactive_map = None
