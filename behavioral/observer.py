"""
Observer

A way of notifying change to a number of classes
"""


class Manager(object):
    """ Subject """
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        if not isinstance(observer, PlayerBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        if observer not in self._observers:
            raise ValueError()
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class PlayerBase(object):
    """ Observer """
    def update(self, data):
        raise NotImplementedError()


class Player(PlayerBase):
    """ Concrete Observer """
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print('{}: {}'.format(self._name, data))


if __name__ == '__main__':
    training = Manager()
    games = Manager()
    alex = Player('Alex')
    nick = Player('Nick')
    training.attach(alex)
    training.attach(nick)
    games.attach(alex)
    training.notify('Training on Sat at 7:30')
    games.notify('Game on Sun at 12:00')
