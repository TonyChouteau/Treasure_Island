from game.map.map import Map
from game.position import Position


class HintDistrict:
    map: Map = Map()

    def __init__(self, id: int) -> None:
        self.id = id

    def is_valid(self, treasure: Position) -> bool:
        return self.id != self.map.which_district(treasure)
