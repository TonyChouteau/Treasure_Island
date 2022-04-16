from game.player.pirate.Pirate import Pirate


class AnneBonny(Pirate):

    def __init__(self, websocket):
        Pirate.__init__(self, "#144bb8", websocket)
