"""
Adapter (aka Wrapper) is structural design pattern.

Allows the interface of the existing class to be used
as another interface.

Usage: an adapter can be used when the wrapper must respect
a particular interface and must support polymorphic behavior.
Convert one interface to another so that it matches what the client is
expecting.

+ allows more flexibility in design
+ handles logic by wrapping a new interface around of an existing class
  that can use new API and avoid breaking existing implementations
+ absolutely interconnects two incompatible interfaces

- unnecessarily increases the size of the code as class inheritance
  is less used and lot of code is needlessly duplicated between classes
- sometimes many adaptations are required along an adaptor chain
  to reach the type which is required
"""

# Realize Object Adapter design pattern
# @TODO: realize Class Adapter design pattern
class Hockey(object):
    def __init__(self, puck):
        self._puck = puck

    def get_puck(self):
        return 'In hockey are played by {}'.format(self._puck)


class Soccer(object):
    def __init__(self, ball):
        self._ball = ball
        print(ball)

    def get_ball(self):
        return 'In soccer are played by {}'.format(self._ball)


class HockeyAdapter(Soccer):
    def __init__(self, puck):
        super(HockeyAdapter, self).__init__(puck)
        self._hockey = Hockey(puck=puck)

    def get_ball(self):
        return self._hockey.get_puck()


if __name__ == '__main__':
    soccer = Soccer('Adidas')
    hockey = HockeyAdapter('Sher-Wood')

    print(soccer.get_ball())
    print(hockey.get_ball())
