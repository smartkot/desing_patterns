"""
Flyweight

Minimizes memory usage by sharing as much data as possible with other
similar objects
"""

import weakref


class Team(object):
    """ Flyweight """
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Game(object):
    """ Flyweight Factory """

    _teams = weakref.WeakValueDictionary()

    @classmethod
    def played_game(cls, name):
        team = cls._teams.get(name)
        if not team:
            team = Team(name)
            cls._teams[name] = team
        return team


if __name__ == '__main__':
    team1 = Game().played_game('Red Team')
    team2 = Game().played_game('Blue Team')
    team3 = Game().played_game('Red Team')
    print(id(team1), id(team2), id(team3))
