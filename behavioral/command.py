"""
Command

Introduces transaction style approach to:
* encapsulate client request by a set of corresponding command objects;
* place command objects in a queue;
* support 'undo' operation by deleting commands from the queue.
"""


class Player(object):
    """ Receiver """
    def shot(self):
        print('Shot on goal')

    def assist(self):
        print('Get assist')

    def stop(self):
        print('No action')


class Command(object):
    """ Base class """
    def __init__(self, player):
        self._player = player

    def execute(self):
        raise NotImplementedError()

    def unexecute(self):
        self._player.stop()


class ShotCommand(Command):
    """ Concrete command """
    def execute(self):
        self._player.shot()


class AssistCommand(Command):
    """ Concrete command """
    def execute(self):
        self._player.assist()


class PlayerInterface(object):
    """ Invoker """
    def __init__(self, shot, assist):
        self.shot_cmd = shot
        self.assist_cmd = assist
        self.current_cmd = None

    def shot(self):
        self.current_cmd = self.shot_cmd
        self.current_cmd.execute()

    def assist(self):
        self.current_cmd = self.assist_cmd
        self.current_cmd.execute()

    def stop(self):
        if self.current_cmd:
            self.current_cmd.unexecute()


if __name__ == '__main__':
    player = Player()
    action = PlayerInterface(ShotCommand(player), AssistCommand(player))
    action.shot()
    action.assist()
    action.stop()
    action.shot()
    action.stop()
