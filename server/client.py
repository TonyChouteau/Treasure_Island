class Client:

    def __init__(self, websocket):
        self.websocket = websocket

        self.username = None
        self.player = None
        self.disconnected = False

    def websocket_equals(self, websocket):
        if self.websocket:
            return self.websocket.id == websocket.id
        else:
            return False

    def set_username(self, username):
        self.username = username

    def set_player(self, player):
        self.player = player

    def disconnect(self):
        self.disconnected = True
        self.websocket = None

    def reconnect(self, websocket):
        self.disconnected = False
        self.websocket = websocket
