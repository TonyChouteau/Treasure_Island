import string

from game.map.InteractiveMap import InteractiveMap


class Player:

    def __init__(self, color: string, websocket):
        self.interactive_map = None
        self.color = color
        self.websocket = websocket
        
    def websocket_equals(self, websocket):
        return self.websocket.id == websocket.id

    def set_interactive_map(self, interactive_map: InteractiveMap):
        self.interactive_map = interactive_map
