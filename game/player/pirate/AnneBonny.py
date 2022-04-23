from game.player.pirate.Pirate import Pirate


class AnneBonny(Pirate):

    id = "anne"
    name = "Anne Bonny"

    def __init__(self):
        Pirate.__init__(self, "#144bb8")
