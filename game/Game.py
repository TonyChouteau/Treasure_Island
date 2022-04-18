import json

from game.player.LongJohn import LongJohn
from game.player.pirate.AnneBonny import AnneBonny
from game.player.pirate.CharlotteDeBerry import CharlotteDeBerry
from game.player.pirate.JimHawkins import JimHawkins
from game.player.pirate.OlivierLevasseur import OlivierLevasseur
from utils.Logger import Logger


class Game:

    def __init__(self):
        self.map = None

        self.clients = []
        self.pirates = []
        self.pirates_names = []
        self.long_john = None

        self.started = False

    def set_map(self, world):
        self.map = world

    def get_player_list(self):
        return [{
            "username": _client.username,
            "pirate": _client.player.name if _client.player is not None else None
        } for _client in self.clients]

    def player_join(self, username, client):
        if client in self.clients:
            return False
        if len(self.clients) <= 5 and self.started is False:
            client.set_username(username)
            self.clients.append(client)
            return True
        return False

    def player_leave(self, client):
        if client not in self.clients:
            return False

        self.clients = [_client for _client in self.clients if _client is not client]
        return True

    def add_pirate(self, pirate_name, client):
        if pirate_name in self.pirates_names or pirate_name == "longjohn" and self.long_john is not None:
            return False

        if pirate_name == "olivier":
            pirate = OlivierLevasseur(client.websocket)
            self.pirates.append(pirate)
            self.pirates_names.append(pirate_name)
        elif pirate_name == "jim":
            pirate = JimHawkins(client.websocket)
            self.pirates.append(pirate)
            self.pirates_names.append(pirate_name)
        elif pirate_name == "charlotte":
            pirate = CharlotteDeBerry(client.websocket)
            self.pirates.append(pirate)
            self.pirates_names.append(pirate_name)
        elif pirate_name == "anne":
            pirate = AnneBonny(client.websocket)
            self.pirates.append(pirate)
            self.pirates_names.append(pirate_name)
        elif pirate_name == "longjohn":
            pirate = LongJohn(client.websocket)
            self.long_john = pirate
        else:
            return False

        client.set_pirate(pirate)

        return True

    def remove_pirate(self, client):
        if self.long_john is not None and self.long_john.websocket_equals(client.websocket):
            self.long_john = None
            return True

        index = -1
        for id in range(len(self.pirates)):
            if self.pirates[id].websocket_equals(client.websocket):
                index = id
        if index != -1:
            self.pirates.pop(index)
            self.pirates_names.pop(index)
            return True
        return False

    def start(self):
        if len(self.pirates) < 1 or self.long_john is None or self.map is None:
            return False

        self.started = True
        Logger.debug("Start", "Game")
        return True
