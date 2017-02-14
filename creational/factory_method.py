"""
Factory Method

Define an interface to create a single object, but let subclasses
decide which class to instance. Factory Method lets a class defer
instantiation to subclasses.

+ allow to make objects code more clearly, not being tied to specific
  classes (ConcreteProduct) and operating with only a common interface
  (Product);
+ allows to set a relationship between a parallel class hierarchy;
- needs to create a child of Creator for each new type of product
  (ConcreteProduct)
"""


# Product
class Competition(object):
    def cup(self):
        raise NotImplementedError()


# Concrete Products
class StanleyCup(Competition):
    def cup(self):
        return "Stanley Cup"


class GagarinCup(Competition):
    def cup(self):
        return "Gagarin Cup"


class OlympicGames(Competition):
    def cup(self):
        return "Olympic Games"


# Creator
class Creator(object):
    def create_cup(self, league):
        raise NotImplementedError()


# Concrete Creator
class HockeyCup(Creator):
    def create_cup(self, league=None):
        """Fabric method"""
        if league == 'NHL':
            return StanleyCup()
        elif league == 'KHL':
            return GagarinCup()
        else:
            return OlympicGames()


if __name__ == '__main__':
    trophy = HockeyCup()
    print(trophy.create_cup('NHL').cup())
    print(trophy.create_cup('KHL').cup())
    print(trophy.create_cup().cup())
