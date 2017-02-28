"""
Decorator (aka Wrapper)

Allows to add extra features to an individual object without affecting
the behavior of other objects from the same class.

+ flexibility, change behavior of object without inheritance
+ very useful as wrapper around application calls
- introduces many small look-alike objects, apps become difficult
  to comprehend and debug
"""


from abc import ABCMeta, abstractmethod


class Team(object):
    """ Component """
    __metaclass__ = ABCMeta

    @abstractmethod
    def compete(self):
        pass


class HockeyTeam(Team):
    """ Concrete Component """

    def compete(self):
        return 'Playing hockey...'


class Bandy(Team):
    """ Decorator """
    def __init__(self, team):
        self._team = team

    def compete(self):
        return self._team.compete() + 'Playing bandy...'


if __name__ == '__main__':
    team = HockeyTeam()
    print(team.compete())
    team = Bandy(team)
    print(team.compete())
