from game.player.pirate.Pirate import Pirate


class OlivierLevasseur(Pirate):

    def __init__(self, websocket):
        Pirate.__init__(self, "#de6c26", websocket)
