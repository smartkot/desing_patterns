"""
Facade

Provides a simplified interface to a lager body of code , such as
a class library. It can:

+ make a software library easier to use, understand and test
+ make the library more readable
+ reduce dependence of outside code on the inner classes
+ wrap with a single designed API
"""


# Parts of complex object
class Player(object):
    def __init__(self):
        self._name = 'Player'

    def play(self):
        print('{}: play game'.format(self._name))

    def cry(self):
        print('{}: need help'.format(self._name))


class Coach(object):
    def __init__(self):
        self._name = 'Coach'

    def make_lineup(self):
        print('{}: define lineup'.format(self._name))

    def make_substitute(self):
        print('{}: make substitute'.format(self._name))


class ServiceKeeper(object):
    def __init__(self):
        self._name = 'ServiceKeeper'

    def get_drink(self):
        print('{}: get drink water'.format(self._name))

    def get_kit(self):
        print('{}: get kit'.format(self._name))


class MedicalStuff(object):
    def __init__(self):
        self._name = 'MedicalStuff'

    def freeze(self):
        print('{}: freeze'.format(self._name))


# Facade
class Team(object):
    def __init__(self):
        self._player = Player()
        self._coach = Coach()
        self._service_keeper = ServiceKeeper()
        self._medical_staff = MedicalStuff()

    def play_game(self):
        self._service_keeper.get_kit()
        self._coach.make_lineup()
        self._player.play()
        self._player.cry()
        self._medical_staff.freeze()
        self._service_keeper.get_drink()
        self._coach.make_substitute()


# Client
if __name__ == '__main__':
    team = Team()
    team.play_game()
