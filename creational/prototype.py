"""
Prototype

It is used when the type of objects to create is determinate
by a prototypical instance, which is cloned to produce a new objects.
"""


import copy


class Prototype(object):
    def __init__(self):
        self._object = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._object[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._object[name]

    def clone(self, name, **kwargs):
        """Clone a registered object and update inner attributes dict"""
        obj = copy.deepcopy(self._object.get(name))
        obj.__dict__.update(kwargs)
        return obj


class Player(object):
    def __init__(self):
        self.player = 'Alex Ovechkin'
        self.goals = 26
        self.assists = 25

    def __str__(self):
        return "{} - Points: {} ({} + {})".format(self.player,
                                                  self.goals+self.assists,
                                                  self.goals,
                                                  self.assists)


if __name__ == '__main__':
    player1 = Player()
    prototype = Prototype()
    prototype.register_object('WSH', player1)
    player2 = prototype.clone('WSH', player='Evgeny Kuznetsov', goals=12, assists=32)
    player3 = prototype.clone('WSH')
    for i in (player1, player2, player3):
        print(i)
