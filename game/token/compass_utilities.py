from game.position import Position
from math import degrees, atan2, floor


def get_direction(player: Position, treasure: Position) -> int:
    angle = degrees(atan2(treasure.y - player.y, treasure.x - player.x))
    offset = (angle + 202.5) / 45  # Offset to get positive angles and 8 directions with diagonal frontiers
    return floor(offset) % 8  # Reduce angle to [0,7] interval, giving the direction


def test_position(player: Position, treasure: Position, direction: int) -> bool:
    return self.get_direction(player, treasure) == direction
