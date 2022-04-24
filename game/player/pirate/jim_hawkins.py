from game.player.pirate.pirate import Pirate


class JimHawkins(Pirate):

    id = "jim"
    name = "Jim Hawkins"

    def __init__(self):
        Pirate.__init__(self, "#207d2a")
