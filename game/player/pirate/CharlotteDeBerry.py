from game.player.pirate.Pirate import Pirate


class CharlotteDeBerry(Pirate):

    id = "charlotte"
    name = "Charlotte De Berry"

    def __init__(self):
        Pirate.__init__(self, "#a81616")
