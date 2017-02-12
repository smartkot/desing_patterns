"""
Abstract factory.

Provide an interface for creating families of related or
dependent objects without specifying their concrete classes.
"""


class AbstractFactory(object):
    def create_phone(self):
        raise NotImplementedError()

    def create_network(self):
        raise NotImplementedError()


class Phone(object):
    def __init__(self, model_name):
        self._model_name = model_name

    def __str__(self):
        return self._model_name


class Network(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactoryBeeline(AbstractFactory):
    def create_phone(self):
        return Phone('SENSEIT_A109')

    def create_network(self):
        return Network('Beeline')


class ConcreteFactoryMegafon(AbstractFactory):
    def create_phone(self):
        return Phone('MFLogin3T')

    def create_network(self):
        return Network('Megafon')


if __name__ == '__main__':
    client = ConcreteFactoryBeeline()
    print(client.create_phone(), client.create_network())
