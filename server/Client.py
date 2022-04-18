class Client:

    def __init__(self, websocket):
        self.websocket = websocket

        self.username = None
        self.player = None

    def set_username(self, username):
        self.username = username

    def set_player(self, player):
        self.player = player

