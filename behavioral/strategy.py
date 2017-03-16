"""
Strategy (aka Policy)

Anables an algorithm's behavior to be selected at runtime.
"""


class GameMode(object):
    """ Strategy Base """
    def play(self):
        raise NotImplementedError()


class Period(GameMode):
    """ Concrete strategy """
    def play(self):
        return 'Playing three periods (5x5)'


class Overtime(GameMode):
    """ Concrete strategy """
    def play(self):
        return 'Playing overtime (3x3)'


class Shootout(GameMode):
    """ Concrete Strategy """
    def play(self):
        return 'Playing shootout (3 bullets)'


class Game(object):
    """ Context """
    def __init__(self, mode):
        self._mode = mode

    def __str__(self):
        return self._mode.play()


if __name__ == '__main__':
    game = Game(Period())
    print(game)
    game = Game(Overtime())
    print(game)
    game = Game(Shootout())
    print(game)
