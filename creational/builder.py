"""
Builder.

Separate the construction of a complex object from its representation.

    + allows to vary a product's internal representation;
    + encapsulates code for construction and representation;
    + provides control over step of a construction process;
    - requires creating a separate ConcreteBuilder for each different types of product.
"""


class Director(object):
    """Controls the construction process"""

    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def get_team(self):
        """"""
        team = Team()

        sport = self._builder.sport
        team.set_sport(sport)

        try:
            goalkeeper = self._builder.get_goalkeeper()
            team.set_goalkeeper(goalkeeper.lineup)
        except AttributeError:
            team.set_goalkeeper(0)

        players = self._builder.get_players()
        for _ in range(players.lineup):
            team.set_player(1)

        return team


class Builder(object):
    """Create parts of a club"""

    def get_goalkeeper(self): pass

    def get_players(self): pass


class Team(object):
    """The complex object"""

    def __init__(self):
        self._sport = None
        self._goalkeeper = None
        self._players = list()

    def set_sport(self, sport):
        self._sport = sport

    def set_goalkeeper(self, player):
        self._goalkeeper = player

    def set_player(self, player):
        self._players.append(player)

    def __str__(self):
        return "{} team consist of {} players".format(self._sport,
                                                      self._goalkeeper + len(self._players))


class Goalkeeper(object):
    lineup = None


class Players(object):
    lineup = None


class HockeyBuilder(Builder):
    """Concrete builder implementation"""
    sport = 'Hockey'

    def get_goalkeeper(self):
        goalkeeper = Goalkeeper()
        goalkeeper.lineup = 1
        return goalkeeper

    def get_players(self):
        players = Players()
        players.lineup = 5
        return players


class RugbyBuilder(Builder):
    """Concrete builder implementation"""
    sport = 'Rugby'

    def get_players(self):
        players = Players()
        players.lineup = 15
        return players

if __name__ == '__main__':
    director = Director()

    hockey_builder = HockeyBuilder()
    director.set_builder(hockey_builder)
    hockey_team = director.get_team()
    print(hockey_team)

    rugby_builder = RugbyBuilder()
    director.set_builder(rugby_builder)
    rugby_team = director.get_team()
    print(rugby_team)
