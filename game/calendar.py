from player import player


class Calendar:
    def __init__(self, players):
        self.players = players
        self.date = 0
        self.starting_blocks = sorted(
            self.players, key=lambda x: x.turnNumber
        )  # Virtual spots before the board for the players, placed by turn order
        self.calendar_board = []  # Board spots (calendar) for players to move in
        self.events = ""  # Chain of event codes in order with the calendar

        if len(self.players) % 2 == 0:  # 2 or 4 players
            self.calendar_board = [0 for _ in range(19)]
            self.events = "1213104502050505000"
        else:
            self.calendar_board = [0 for _ in range(17)]
            self.events = "12130145250550000"

    def next(self):
        # Move the players around
        if len(self.starting_blocks) != 0:
            self.calendar_board[self.date] = self.starting_blocks.pop()
        else:
            self.calendar_board[self.date] = self.calendar_board[
                self.date - len(self.players)
            ]
            self.calendar_board[self.date - len(self.players)] = 0

        self.date += 1
        if self.date > len(self.calendar_board):
            pass  # end
        if self.events[self.date] != 0:
            pass  # Handle various events
