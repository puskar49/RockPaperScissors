from throw import Rock, Paper, Scissors
import random

THROW_INDEX = ["R", "P", "S"]


class Player(object):
    def __init__(self):
        self._name = None
        self._wins = 0
        self._throws = [Rock(), Paper(), Scissors()]

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._wins

    def throw(self):
        pass

    def win(self):
        self._wins += 1


class CPU(Player):
    def __init__(self):
        super().__init__()
        self._name = "CPU"

    def throw(self):
        return self._throws[random.randrange(3)]


class Human(Player):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def throw(self):
        while True:
            try:
                t = input("[R]ock, [P]aper, or [S]cissors? ")
                return self._throws[THROW_INDEX.index(t.upper()[0])]
            except (IndexError, KeyError, ValueError):
                pass
