from typing import Type

class Prompt:
    def __init__(self, qty: int, type: Type):
        self.memory = []
        self.qty = qty
        self.type = type

    def add(self, element):
        if type(element) != self.type :
            # raise error
            pass
        else :
            self.memory.append(element)

    def get(self):
        return self.memory

    def resolved(self):
        return len(self.memory) == self.qty
