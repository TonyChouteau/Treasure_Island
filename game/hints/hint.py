from typing import Callable
from game.hints.prompt import Prompt
from game.map.map import Map
from game.map.zone import Zone


class Hint:
    map_: Map

    def __init__(self, name: str, predicate: Callable, prompts: list[Prompt]):
        self.name: str = name
        self.predicate: Callable = predicate
        self.prompts: list = prompts
        self.current_prompt: int = 0
        self.lie: bool = False  # TODO

    def get_current_prompt(self) -> Prompt:
        return self.prompts[self.current_prompt]

    def solve_prompt(self, selection: list) -> bool:
        for element in selection:
            self.get_current_prompt().add(element)
        if self.get_current_prompt().resolved():
            self.current_prompt += 1
        return self.current_prompt >= len(self.prompts)

    def check_predicate(self, selection: list) -> bool:
        return self.lie or self.predicate(selection, self.map_)


WHITE_HINT_PILE = []


def pred_altitude(selection: list, map_: Map):
    if selection[0] == Zone.VOLCANO:
        return map_.which_zone(map_.treasure).is_volcano()
    elif selection[0] == Zone.TEMPLE:
        return map_.which_zone(map_.treasure).is_temple()
    elif selection[0] == Zone.COAST:
        return map_.which_zone(map_.treasure).is_coast()


WHITE_HINT_PILE.append(
    Hint(
        "Altitude",
        pred_altitude,
        [Prompt(1, type(Zone))]
    )
)
