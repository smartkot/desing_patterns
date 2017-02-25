"""
Composite

Describes that a group of objects is to be treated in a same way as
a single instance of an object.

Usage: when dealing with tree-structured data to allow treating complex
and primitive objects uniformly.

+ Clients use the Component class interface to interact with objects
  in composite structure.
+ Calls to a Leaf handles directly.
+ Calls to a Composite forwards the request to its child components.

- Once tree structure is defined^ the composite design makes the tree
  overly general.
- It is difficult to restrict the components of the tree to only
  particular types.
- To enforce such constraint the program must rely on run-time checks.
"""


class Club(object):
    """ Component """
    def __str__(self):
        raise NotImplementedError()


class Coach(Club):
    """ Leaf Coach """
    def __init__(self, position):
        self._position = position

    def __str__(self):
        return self._position


class Goalkeeper(Club):
    """ Leaf Goalkeeper """
    def __init__(self):
        self._position = 'Goalkeeper'

    def __str__(self):
        return 'Goalkeeper'


class Player(Club):
    """ Leaf Player """
    def __init__(self, position):
        self._position = position

    def __str__(self):
        return self._position


class Team(Club):
    """ Composite """
    def __init__(self):
        self._roster = []

    def __str__(self):
        for player in self._roster:
            print(player, end=', ')
        return '(id team: {})'.format(self.__hash__())

    def add(self, member):
        self._roster.append(member)
        print('Adding {} from the team (id: {})'.format(member, self.__hash__()))

    def remove(self, member):
        try:
            self._roster.remove(member)
            print('Removing {} from the team (id: {})'.format(member, self.__hash__()))
        except ValueError as e:
            print('{} not found at the teem'.format(member))


if __name__ == '__main__':
    torpedo = Team()
    goalkeeper = Goalkeeper()
    defender = Player('Defender')
    center = Player('Center Forward')
    left_wing = Player('Left Wing Forward')
    torpedo.add(goalkeeper)
    torpedo.add(defender)
    torpedo.add(center)
    torpedo.add(left_wing)
    print(torpedo)
    print()
    staff = Team()
    head_coach = Coach('Head Coach')
    coach = Coach('Coach')
    staff.add(head_coach)
    staff.add(coach)
    print(staff)
    print()
    torpedo.remove(left_wing)
    torpedo.remove(left_wing)
    torpedo.add(staff)
    print(torpedo)
