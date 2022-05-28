from game.game import Game
from utils.logger import Logger


class Routes:

    def __init__(self):
        # Define all routes
        self.route = {
            "player_join": self.player_join,
            "select_pirate": self.select_pirate,
            "unselect_player": self.unselect_pirate,
            "chat_message": self.chat_message,
            "player_ready": self.player_ready
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

    # Disconnect

    def disconnect(self, client):
        result = self.game.player_leave(client)
        Logger.debug(result, "player leave")
        return {
            "broadcast": self.get_players_data()
        }

    def reconnect(self, username):
        for _client in self.get_clients():
            if _client.disconnected and _client.username == username:
                return _client
        return None

    # Getters

    def get_clients(self):
        return self.game.get_clients()

    def get_client(self, websocket):
        return self.game.get_client(websocket)

    # Data Formatting

    def get_players_data(self):
        return {
            "type": "player_list",
            "data": self.game.get_player_list_dict()
        }

    def get_reconnect_data(self, client):
        return {
            "type": "reconnect_select",
            "data": {
                "list": self.game.get_player_list_dict(),
                "selected": client.player.id if client.player is not None else None
            },
        }

    @staticmethod
    def get_chat_message_data(data, client):
        Logger.debug(data.get("new_message"), "Message")
        return {
            "type": "chat_message",
            "data": {
                "sender": client.username if not data.get("game_message", False) else "game",
                "message": data.get("new_message")
            }
        }

    # Routes

    def player_join(self, data, client):
        # TODO : Better handling of html/js/css injection
        username = data.get("username")

        reconnected_client = self.reconnect(username)
        if reconnected_client:
            reconnected_client.reconnect(client.websocket)
            client = reconnected_client

            return {
                "for_client": {
                    client: self.get_reconnect_data(client)
                },
                "broadcast": self.get_players_data()
            }

        if "(" in username or "{" in username or "\"" in username \
                or "=" in username or "<" in username or username == "":
            return False

        if username in [_client.username for _client in self.game.get_clients() if not _client.disconnected]:
            return False
        result = self.game.player_join(username, client)
        Logger.debug(result, "player join")
        return {
            "broadcast": self.get_players_data()
        }

    def select_pirate(self, data, client):
        self.game.remove_pirate(client)
        self.game.add_pirate(data.get("pirate_name"), client)
        Logger.debug(self.game.get_player_list_dict(), "pirates")
        return {
            "broadcast": self.get_players_data()
        }

    def unselect_pirate(self, data, client):
        self.game.remove_pirate(client)
        return {
            "broadcast": self.get_players_data()
        }

    def chat_message(self, data, client):
        # TODO : HANDLE INJECTION
        return {
            "broadcast": self.get_chat_message_data(data, client)
        }

    def player_ready(self, data, client):
        client.ready = data.get("ready")
        return {
            "broadcast": self.get_players_data()
        }
