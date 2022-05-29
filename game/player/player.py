from game.position import Position

from game.map.interactive_map import InteractiveMap


class Player:
    
    id : str
    name : str
    position : Position
    color : str
    interactive_map : InteractiveMap
    
    def __init__(self, color: str):#, turnNumber: int):
        self.interactive_map = None
        self.color = color
        self.name = None
        self.position = None
        #self.turnNumber = turnNumber

    def set_interactive_map(self, interactive_map: InteractiveMap):
        self.interactive_map = interactive_map

    # def setTurn(self, turnNumber: int):
    #     self.turnNumber = turnNumber
    
    def move():
        pass
