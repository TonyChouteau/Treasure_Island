from game.player.LongJohn import LongJohn
from game.player.pirate.AnneBonny import AnneBonny
from game.player.pirate.CharlotteDeBerry import CharlotteDeBerry
from game.player.pirate.JimHawkins import JimHawkins
from game.player.pirate.OlivierLevasseur import OlivierLevasseur


class Game:

    def __init__(self):
        self.map = None

        self.pirates = []
        self.pirates_names = []
        self.long_john = None

    def set_map(self, world):
        self.map = world

    def add_pirate(self, pirate_name, websocket):
        if pirate_name in self.pirates_names:
            return False

        if pirate_name == "olivier":
            self.pirates.append(OlivierLevasseur(websocket))
            self.pirates_names.append(pirate_name)
        elif pirate_name == "jim":
            self.pirates.append(JimHawkins(websocket))
            self.pirates_names.append(pirate_name)
        elif pirate_name == "charlotte":
            self.pirates.append(CharlotteDeBerry(websocket))
            self.pirates_names.append(pirate_name)
        elif pirate_name == "anne":
            self.pirates.append(AnneBonny(websocket))
            self.pirates_names.append(pirate_name)
        elif pirate_name == "longjohn":
            self.long_john = LongJohn(websocket)
        else:
            return False
        return True

    def remove_pirate(self, websocket):
        if self.long_john is not None and self.long_john.websocket_equals(websocket):
            self.long_john = None
            return True

        index = -1
        for id in range(len(self.pirates)):
            if self.pirates[id].websocket_equals(websocket):
                index = id
        if index != -1:
            self.pirates.pop(index)
            self.pirates_names.pop(index)
            return True
        return False

    def start(self):
        if len(self.pirates) < 1 or self.long_john is None or self.map is None:
            return False

        print("Start")
        return True
