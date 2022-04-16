from game.player.Player import Player


class Pirate(Player):

    def __init__(self, color, websocket):
        Player.__init__(self, color, websocket)
        self.interactive_map = None
