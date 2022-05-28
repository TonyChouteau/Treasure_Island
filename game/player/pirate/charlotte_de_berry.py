from game.player.pirate.pirate import Pirate


class CharlotteDeBerry(Pirate):

    def __init__(self):
        Pirate.__init__(self, "#a81616")
        self.id = "charlotte"
        self.name = "Charlotte De Berry"
        
    def get_distric_hints():
        pass
