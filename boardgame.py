#contain boardgame class
class BoardGame:
    def __init__(self, title, publisher, year, players, playing_time):
        self.title = title
        self.publisher = publisher
        self.year = year
        self.players = players
        self.playing_time = playing_time