from typing import Type


class Prompt:
    def __init__(self, qty: int, type_: Type):
        self.memory = []
        self.qty = qty
        self.type_ = type_

    def add(self, element):
        if type(element) != self.type_:
            # raise error
            pass
        else:
            self.memory.append(element)

    def resolved(self) -> bool:
        return len(self.memory) == self.qty
