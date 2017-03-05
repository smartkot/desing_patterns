"""
Chain of responsibility

Used to process varied requests, each of which may be dealt
with a different handler.
"""


class TrainingHandler(object):
    """ Interface Handler """
    def is_train(self):
        raise NotImplementedError()


class PhysicalTrainingHandler(TrainingHandler):
    """ Concrete Handler """
    def is_train(self):
        print('Physical exercises')


class TacticalTrainingHandler(TrainingHandler):
    """ Concrete Handler """
    def is_train(self):
        print('Tactical lessons')


class Team(object):
    """ Client """
    def __init__(self):
        self._handlers = set()

    def add_handler(self, handler):
        self._handlers.add(handler)

    def train(self):
        for handler in self._handlers:
            handler.is_train()


if __name__ == '__main__':
    team = Team()
    team.add_handler(PhysicalTrainingHandler())
    team.add_handler(TacticalTrainingHandler())
    team.train()
