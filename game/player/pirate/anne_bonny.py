from game.player.pirate.pirate import Pirate


class AnneBonny(Pirate):

    id = "anne"
    name = "Anne Bonny"

    def __init__(self):
        Pirate.__init__(self, "#144bb8")
