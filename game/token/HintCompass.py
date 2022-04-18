from game.token import Compass
from game.Position import Position

class HintCompass(Compass):

    def __init__(self, direction1: int, direction2: int) -> None:
        super().__init__()
        self.direction1 = direction1
        self.direction2 = direction2

    def is_valid(self, player: Position, treasure: Position) -> bool:
        dir1 = self.test_position(player,treasure,self.direction1) 
        dir2 = self.test_position(player,treasure,self.direction2) 
        return dir1 or dir2