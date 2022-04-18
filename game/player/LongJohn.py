from game.player.Player import Player


class LongJohn(Player):

    name = "Long John"

    def __init__(self, websocket):
        Player.__init__(self, "#000000", websocket)