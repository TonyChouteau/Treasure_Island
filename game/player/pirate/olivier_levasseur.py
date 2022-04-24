from game.player.pirate.pirate import Pirate


class OlivierLevasseur(Pirate):

    id = "olivier"
    name = "Olivier Levasseur"

    def __init__(self):
        Pirate.__init__(self, "#de6c26")
