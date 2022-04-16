from game.Game import Game
from utils.Logger import Logger


class Routes:

    def __init__(self):
        # Define all routes
        self.route = {
            "select_pirate": self.select_pirate
        }

        self.game = Game()

    # Check the availability of the route
    def exists(self, event_type):
        return True if self.route.get(event_type) else False

    # Handle route access
    def handle(self, data_type, data, websocket):
        if self.exists(data_type):
            result = self.route.get(data_type)(data, websocket)
            Logger.debug(result, "Routes")

    def disconnect(self, websocket):
        # TODO : Handle deco/reco
        result = self.game.remove_pirate(websocket)
        Logger.debug(result, "Routes")

    # Routes
    def select_pirate(self, data, websocket):
        self.game.remove_pirate(websocket)
        return self.game.add_pirate(data.get("pirate_name"), websocket)
