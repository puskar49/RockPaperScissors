class Throw(object):
    def __init__(self):
        self._value = None
        self._name = None

    def __gt__(self, other):
        if not isinstance(other, Throw):
            return NotImplemented
        x = self._value - other._value
        return x == -1 or x == 2

    @property
    def name(self):
        return self._name


class Scissors(Throw):
    def __init__(self):
        super().__init__()
        self._value = -1
        self._name = "Scissors"


class Paper(Throw):
    def __init__(self):
        super().__init__()
        self._value = 0
        self._name = "Paper"


class Rock(Throw):
    def __init__(self):
        super().__init__()
        self._value = 1
        self._name = "Rock"
