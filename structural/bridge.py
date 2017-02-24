"""
Bridge (aka Handle/Body).

'Decouple an abstraction from its implementation, so that the two can
vary independently.' Gang of Four

The pattern is designed to separate a class's interface from its
implementation so you can vary or replace implementation code without
changed the client code.
"""


class GameBase(object):
    """ Implementor """
    def duration(self, time):
        raise NotImplementedError()


class RugbyGame(GameBase):
    """ Concrete Implementor A"""
    def duration(self, time):
        print('Duration of rugby game is {} minutes'.format(time))


class HockeyGame(GameBase):
    """ Concrete Implementor B"""
    def duration(self, time):
        print('Duration of hockey game is {} minutes'.format(time))


class TVProgramBase(object):
    """ Abstraction """
    def __init__(self):
        self._game = self.get_game()

    def get_game(self):
        raise NotImplementedError()

    def get_duration(self, time):
        self._game.duration(time)


class TVProgram(TVProgramBase):
    """ RefinedAbstraction """
    def __init__(self):
        super(TVProgram, self).__init__()

    def get_game(self):
        return RugbyGame()


if __name__ == '__main__':
    tv_program = TVProgram()
    tv_program.get_duration(80)