from bowling.game import Game


def main():
    game = Game()
    with open('input') as f:
        for line in f:
            try:
                pins = int(line)
                game.roll(pins)
            except ValueError:
                print str(line) + " is not a number"
                print "score up to this line: " + str(game.score)
                return
    with open('output', 'w') as f:
        f.write(str(game.score) + "\n")
    pass


if __name__ == "__main__":
    main()