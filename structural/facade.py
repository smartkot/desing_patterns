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
    def play(self):
        print('Player: play game')

    def cry(self):
        print('Player: need help')


class Coach(object):
    def make_lineup(self):
        print('Coach: define lineup')

    def make_substitute(self):
        print('Player: make substitute')


class ServiceKeeper(object):
    def get_drink(self):
        print('ServiceKeeper: get drink water')

    def get_kit(self):
        print('ServiceKeeper: get kit')


class MedicalStuff(object):
    def freeze(self):
        print('MedicalStuff: freeze')


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
