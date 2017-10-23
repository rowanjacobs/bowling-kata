

class Game(object):
    def __init__(self):
        self.score = 0

    def roll(self, pins):
        self.score += pins
        return self.score + pins
