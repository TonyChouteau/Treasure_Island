from player import Player


class Calendar:
    def __init__(self, players):
        self.players = players
        self.date = 0
        self.startingBlocks = sorted(self.players, key=lambda x: x.turnNumber)
        self.calendarBoard = []
        self.events = ""
        if len(self.players) % 2 == 0:
            self.calendarBoard = [0 for _ in range(19)]
            self.events = "1213104502050505000"
        else:
            self.calendarBoard = [0 for _ in range(17)]
            self.events = "12130145250550000"

    def next(self):
        if len(self.startingBlocks) != 0:
            self.calendarBoard[self.date] = self.startingBlocks.pop()
        else:
            self.calendarBoard[self.date] = self.calendarBoard[
                self.date - len(self.players)
            ]
            self.calendarBoard[self.date - len(self.players)] = 0
            
        self.date += 1
        if self.date > len(self.calendarBoard):
            pass  # end
        if self.events[self.date] != 0:
            pass  # Handle various events
