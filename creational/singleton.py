"""
Singleton

Ensure that only one instance of the singleton class ever exists, and
provide a global access to that instance.
"""


def singleton(cls):
    instance = {}

    def get_instance(*args):
        if cls not in instance:
            instance[cls] = cls(*args)
        return instance[cls]
    return get_instance


@singleton
class Captain(object):
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def __str__(self):
        return "{} ({})".format(self.name, self.team)

if __name__ == '__main__':
    player1 = Captain('Alex Ovechkin', 'RUS')
    player2 = Captain('Pavel Datsyuk', 'RUS')

    print(player1, id(player1))
    print(player2, id(player2))
