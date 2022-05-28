from enum import Enum

class Zone(Enum):
    NONE = 0
    LIMIT = 1
    VOLCANO = 2
    TEMPLE = 3
    COAST = 4
    VOLCANO_AND_TEMPLE = 5
    VOLCANO_AND_COAST = 6
    TEMPLE_AND_COAST = 7

    def is_volcano(self) -> bool:
        return self == self.VOLCANO or self == self.VOLCANO_AND_COAST or self == self.VOLCANO_AND_TEMPLE

    def is_temple(self) -> bool:
        return self == self.TEMPLE or self == self.VOLCANO_AND_TEMPLE or self == self.TEMPLE_AND_COAST

    def is_coast(self) -> bool:
        return self == self.COAST or self == self.VOLCANO_AND_COAST or self == self.TEMPLE_AND_COAST
