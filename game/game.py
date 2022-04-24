from game.player.long_john import LongJohn
from game.player.pirate.anne_bonny import AnneBonny
from game.player.pirate.charlotte_de_berry import CharlotteDeBerry
from game.player.pirate.jim_hawkins import JimHawkins
from game.player.pirate.olivier_levasseur import OlivierLevasseur
from utils.Logger import Logger


class Game:

    def __init__(self):
        self.map = None

        self.clients = []
        self.pirates = []
        self.long_john = None

        self.started = False

    def set_map(self, world):
        self.map = world

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

        if not self.started:
            self.clients = [_client for _client in self.clients if _client is not client]
        else:
            client.disconnect()
        return True

    def add_pirate(self, pirate_name, client):
        if pirate_name == "longjohn" and self.long_john is not None \
                or pirate_name in self.get_pirate_name_list():
            return False

        if pirate_name == "olivier":
            pirate = OlivierLevasseur()
            self.pirates.append(pirate)
        elif pirate_name == "jim":
            pirate = JimHawkins()
            self.pirates.append(pirate)
        elif pirate_name == "charlotte":
            pirate = CharlotteDeBerry()
            self.pirates.append(pirate)
        elif pirate_name == "anne":
            pirate = AnneBonny()
            self.pirates.append(pirate)
        elif pirate_name == "longjohn":
            pirate = LongJohn()
            self.long_john = pirate
        else:
            return False

        client.set_player(pirate)

        return True

    def remove_pirate(self, client):
        if client.player is not None:
            if self.long_john == client.player:
                self.long_john = None
            else:
                self.pirates = [_pirate for _pirate in self.pirates if _pirate != client.player]
            client.set_player(None)
            return True
        return False

    def start(self):
        if len(self.pirates) < 1 or self.long_john is None: # or self.map is None:
            return False

        self.started = True
        Logger.debug("Start", "Game")
        return True

    # Getters

    def get_clients(self):
        return self.clients

    def get_client(self, websocket):
        clients = [_client for _client in self.clients if _client.websocket_equals(websocket)]
        if len(clients) == 1:
            return clients[0]
        else:
            return None

    def get_pirate_name_list(self):
        return [_client.player.id for _client in self.clients if _client.player is not None]

    def get_player_list_dict(self):
        return [{
            "username": _client.username,
            "pirate": _client.player.id if _client.player is not None else None,
            "full_name": _client.player.name if _client.player is not None else None,
        } for _client in self.clients]
