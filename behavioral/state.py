"""
Observer

Implements a state machine in object-oriented way.
"""


class State(object):
    """ Base State """
    def play(self):
        raise NotImplementedError()

    def train(self):
        raise NotImplementedError()


class NormalState(State):
    """ Concrete State """
    def play(self):
        return ' is ready to play'

    def train(self):
        return ' is ready to train'


class InjuryState(State):
    """ Concrete State """
    def play(self):
        return ' is injured'

    def train(self):
        return ' is injured'


class DisqualificationState(State):
    """ Concrete State """
    def play(self):
        return ' is no legal to play'

    def train(self):
        return ' is ready to train'


class Player(object):
    """ Context """
    def __init__(self, name, state):
        self._name = name
        self._state = state

    def change_state(self, state):
        self._state = state

    def play(self):
        print(self._name + self._state.play())

    def train(self):
        print(self._name + self._state.train())


if __name__ == '__main__':
    nick = Player('Nick', NormalState())
    nick.play()
    nick.train()
    nick.change_state(DisqualificationState())
    nick.play()
    nick.train()
    nick.change_state(InjuryState())
    nick.play()
    nick.train()
