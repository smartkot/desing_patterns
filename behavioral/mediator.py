"""
Mediator (aka Token)

Defines simplified communication between classes.
"""

import inspect


class GameMode(object):
    """ Mediator """
    def make_pass(self):
        raise NotImplementedError()


class Player(object):
    """ Colleague """
    def __init__(self, mediator):
        self._mediator = mediator

    def give_puck(self):
        raise NotImplementedError()

    def get_puck(self):
        raise NotImplementedError()


class Training(GameMode):
    """ Concrete Mediator """
    def __init__(self):
        self._first = None
        self._second = None

    def set_players(self, first, second):
        self._first = first
        self._second = second

    def make_pass(self):
        maker = inspect.currentframe().f_back.f_locals['self']
        getter = self._first if maker == self._second else self._second
        getter.give_puck()


class Defender(Player):
    """ Concrete Colleague """
    def give_puck(self):
        print('Defender give a puck')

    def get_puck(self):
        print('Defender get a puck')
        self._mediator.make_pass()


class Forward(Player):
    """ Concrete Colleague """

    def give_puck(self):
        print('Forward give a puck')

    def get_puck(self):
        print('Forward get a puck')
        self._mediator.make_pass()


if __name__ == '__main__':
    assists = Training()
    defender = Defender(assists)
    forward = Forward(assists)
    assists.set_players(defender, forward)
    defender.get_puck()
    forward.get_puck()
