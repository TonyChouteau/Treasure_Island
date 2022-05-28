
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
            self.events = "1213104102010101000"
        else:
            self.calendar_board = [0 for _ in range(17)]
            self.events = "12130141210110000"

    def next(self):
        # Move the players around
        if len(self.starting_blocks) != 0:
            self.calendar_board[self.date] = self.starting_blocks.pop()
        else:
            self.calendar_board[self.date] = self.calendar_board[
                self.date - len(self.players)
            ]
            self.calendar_board[self.date - len(self.players)] = 0
            self.play_event(self.date)
            self.date += 1

    def play_event(self, event_date):
        if event_date == len(self.calendar_board):
            pass  # Release LJS : continue playing until someone wins
        else:
            event = self.events[event_date]
            if event == 1:
                pass # LJS chooses a hint (black marked or not) from his hand to reveal and play
                # long_john.play_hint()
            elif event == 2:
                pass # LJS gets a bluff
                # long_john.add_bluff()
            elif event == 3:
                pass # The player activating this event choses one of the 9 jails to place LJS on. 
            elif event == 4:
                pass # LJS discards his hand and draws 3 black marked hints
            else:
                pass