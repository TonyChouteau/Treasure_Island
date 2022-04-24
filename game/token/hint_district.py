from game.position import Position


class HintDistrict:
    def __init__(self, id: int) -> None:
        self.id = id

    def get_district(self, point: Position) -> int:
        # return map(point.x, point.y)["district"]
        return -1

    def is_valid(self, treasure: Position) -> bool:
        return self.id != self.get_district(treasure)
