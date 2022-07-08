from typing import Callable


class Hint:
    def __init__(self, predicate: Callable, prompt: Prompt):
        self.predicate = predicate
        self.prompt = prompt
