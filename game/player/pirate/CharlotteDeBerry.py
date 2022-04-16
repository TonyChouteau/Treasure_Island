from game.player.pirate.Pirate import Pirate


class CharlotteDeBerry(Pirate):

    def __init__(self, websocket):
        Pirate.__init__(self, "#a81616", websocket)
