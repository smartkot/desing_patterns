"""
Memento

Provides the ability an object to its previous state (undo via rollback)
"""


class SavedGame(object):
    """ Memento """
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class GamePlayer(object):
    """ Caretaker """
    def __init__(self):
        self._memento = None

    def get_memento(self):
        return self._memento

    def set_memento(self, memento):
        self._memento = memento


class GameCampaign(object):
    """ Originator """
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_game(self):
        return SavedGame(self._state)

    def undo_game(self, memento):
        self._state =  memento.get_state()


if __name__ == '__main__':
    campaign = GameCampaign()
    player = GamePlayer()

    campaign.set_state('First Round')
    print(campaign.get_state())

    campaign.set_state('Second Round')
    player.set_memento(campaign.save_game())
    print(campaign.get_state())

    campaign.set_state('Conference Finals')
    print(campaign.get_state())

    campaign.undo_game(player.get_memento())
    print(campaign.get_state())
