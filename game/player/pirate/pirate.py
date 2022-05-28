from game.player.player import Player
from game.map.pirate_map import PirateMap
from token.compass import Compass


class Pirate(Player):

    personal_map : PirateMap
    personal_skill_used : bool
    compass_used : bool
    full_galop_used : bool
    hints_to_check : int

    def __init__(self, color):
        Player.__init__(self, color)
        self.personal_map = None
        self.personal_skill_used = False
        self.compass_used = False
        self.full_galop_used = False
        self.hints_to_check = 2
        
    def search(void : bool): #Should be SearchResult
        pass
    
    def move_and_search(void : bool): #Should be SearchResult
        pass
    
    def check_hint(int : bool):
        pass
    
    def full_gallop():
        pass
    
    def use_compass(void : Compass):
        pass
    
