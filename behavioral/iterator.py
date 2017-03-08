"""
Iterator (aka Cursor)

Allows to travers a container and access the container's elements.
"""


class Iterator(object):
    """ Iterator Interface """
    def current_item(self):
        raise NotImplementedError()

    def is_done(self, index):
        raise NotImplementedError()

    def first(self):
        raise NotImplementedError()

    def last(self):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()

    def prev(self):
        raise NotImplementedError()


class PlayerIterator(Iterator):
    """ Concrete Iterator """
    def __init__(self, team=None):
        self._team = team or ['G', 'D1', 'D2', 'LW', 'C', 'RW']
        self._current = 0

    def current_item(self):
        return self._team[self._current]

    def is_done(self, index):
        return 0 <= index <= len(self._team) - 1

    def first(self):
        return self._team[self._current]

    def last(self):
        self._current = len(self._team) - 1
        return self._team[self._current]

    def next(self):
        self._current += 1
        if not self.is_done(self._current):
            self._current = 0
        return self._team[self._current]

    def prev(self):
        self._current -= 1
        if not self.is_done(self._current):
            self._current = len(self._team) - 1
        return self._team[self._current]

# Concrete Aggregate
if __name__ == '__main__':
    hockey_team = PlayerIterator()
    print('Start: ' + hockey_team.first())
    print('Next player: ' + hockey_team.next())
    print('Next player: ' + hockey_team.next())
    print('Rewind: ' + hockey_team.last())
    print('Prev player: ' + hockey_team.prev())
    print('Next player: ' + hockey_team.next())
    print('Next player: ' + hockey_team.next())
