from game.Game import Game
from utils.Logger import Logger


class Routes:

    def __init__(self):
        # Define all routes
        self.route = {
            "player_join": self.player_join,
            "select_pirate": self.select_pirate
        }

        self.game = Game()

    # Check the availability of the route
    def exists(self, event_type):
        return True if self.route.get(event_type) else False

    # Handle route access
    def handle(self, data_type, data, client):
        if self.exists(data_type):
            result = self.route.get(data_type)(data, client)
            Logger.debug(result, "Routes")
            return result

    def disconnect(self, client):
        # TODO : Handle deco/reco
        result = self.game.player_leave(client)
        Logger.debug(result, "Player leave")
        result2 = self.game.remove_pirate(client)
        Logger.debug(result, "remove pirates")
        return {
            "type": "player_list",
            "data": self.game.get_player_list()
        }

    # Routes
    def player_join(self, username, client):
        # TODO : Better handling of html/js/css injection
        if "(" in username or "{" in username or "\"" in username \
                or "=" in username or "<" in username or username == "":
            return False

        result = self.game.player_join(username, client)
        Logger.debug(result, "player join")
        return {
            "type": "player_list",
            "data": self.game.get_player_list()
        }

    def select_pirate(self, data, client):
        self.game.remove_pirate(client)
        return self.game.add_pirate(data.get("pirate_name"), client)
