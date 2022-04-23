from game.player.pirate.Pirate import Pirate


class JimHawkins(Pirate):

    id = "jim"
    name = "Jim Hawkins"

    def __init__(self):
        Pirate.__init__(self, "#207d2a")
