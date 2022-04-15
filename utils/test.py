from game.Game import Game
from game.map.Map import Map
from game.player.LongJohn import LongJohn

from game.player.pirate.CharlotteDeBerry import CharlotteDeBerry
from game.player.pirate.OlivierLevasseur import OlivierLevasseur

world = Map("default")

p1 = OlivierLevasseur()
p2 = CharlotteDeBerry()

lj = LongJohn()

game = Game(world, [p1, p2], lj)

pass
