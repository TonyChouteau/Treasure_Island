import string

from game.map.InteractiveMap import InteractiveMap


class Player:

    def __init__(self, color: string):
        self.interactive_map = None
        self.color = color

    def set_interactive_map(self, interactive_map: InteractiveMap):
        self.interactive_map = interactive_map
