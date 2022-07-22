from typing import Callable
from game.hints.prompt import Prompt
from game.map.map import Map
from game.map.zone import Zone


class Hint:
    map: Map

    def __init__(self, name: str, predicate: Callable, prompt: Prompt):
        self.name = name
        self.predicate = predicate
        self.prompt = prompt

WHITE_HINT_PILE = []

def pred_altitude(selection: list, map: Map):
    if selection[0] == Zone.VOLCANO :
        # FIXME
        return map.which_zone(map.treasure).is_volcano()
    elif selection[0] == Zone.TEMPLE :
        return map.which_zone(map.treasure).is_temple()
    elif selection[0] == Zone.COAST :
        return map.which_zone(map.treasure).is_coast()

WHITE_HINT_PILE.append(
    Hint(
        "Altitude",
        pred_altitude,
        Prompt(1, type(Zone))
    )
)
