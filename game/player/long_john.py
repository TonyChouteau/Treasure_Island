from game.player.player import Player


class LongJohn(Player):

    id = "longjohn"
    name = "Long John"

    def __init__(self):
        Player.__init__(self, "#000000")