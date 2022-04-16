from game.player.pirate.Pirate import Pirate


class JimHawkins(Pirate):

    def __init__(self, websocket):
        Pirate.__init__(self, "#207d2a", websocket)
