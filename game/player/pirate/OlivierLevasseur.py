from game.player.pirate.Pirate import Pirate


class OlivierLevasseur(Pirate):

    id = "olivier"
    name = "Olivier Levasseur"

    def __init__(self):
        Pirate.__init__(self, "#de6c26")
