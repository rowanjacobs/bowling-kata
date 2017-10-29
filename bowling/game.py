

class Game(object):
    def __init__(self):
        self.score = 0
        self.frame = 0
        self.rolls = 0
        self.frameScore = 0

    def roll(self, pins):
        if pins > 10:
            raise ValueError
        self.frameScore += pins
        if self.frameScore > 10:
            raise ValueError
        self.rolls += 1
        if self.rolls % 2 == 0:
            self.frame += 1
            if self.frame >= 10:
                raise IndexError
            self.frameScore = 0
        self.score += pins
        return self.score + pins
