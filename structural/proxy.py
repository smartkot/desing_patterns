#!/usr/bin/env python
# coding=utf-8

"""
Proxy

It is a wrapper or agent object that is being called by the client
to access the real service object behind the scene.

+ REMOTE PROXY can hide the fact, that object resides in a different
  address space
+ VIRTUAL PROXY can perform organizations to create an object on demand
+ PROTECTED PROXY can check the permission for calling an object
+ SMART REFERENCE allows additional housekeeping tasks when an object
  is accessed

- increase in response time
"""


class ITeam(object):
    """ Interface Subject """
    def is_played(self):
        raise NotImplementedError()

    def get_roster(self):
        raise NotImplementedError()


class Team(ITeam):
    """ Real Subject """
    def is_played(self):
        return 'Team {} is played'.format(id(self))

    def get_roster(self):
        # Complex operation, request to DB or something else
        return 'Roster of {} team: ...'.format(id(self))


class ProxyTeam(ITeam):
    """ Proxy """
    def __init__(self):
        self.team = None

    def is_played(self):
        if not self.team:
            return 'Team {} is played'.format(id(self))
        else:
            return self.team.is_played()

    def get_roster(self):
        self.team = Team()
        return self.team.get_roster()


if __name__ == '__main__':
    team = ProxyTeam()
    print(team.is_played())
    print(team.get_roster())
    print(team.is_played())
