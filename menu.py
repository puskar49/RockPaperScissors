class Menu(object):

    def __init__(self):
        self._play = True

    @property
    def play(self):
        return self._play

    @staticmethod
    def announce(player, throw):
        print("{} throws {}".format(player.name, throw.name))

    def end_round(self):
        self._play = None
        while self._play is None:
            play_again = input("Play again? (Y/n) ").upper()
            if play_again == "Y" or play_again == "" or play_again == "YES":
                self._play = True
            elif play_again == "N" or play_again == "NO":
                self._play = False

    def greet(self):
        print("Welcome to Rock, Paper, Scissors!")
        name = None
        while not self.is_valid_name(name):
            name = input("What shall I call you? ")
        return name

    @staticmethod
    def score(player1, player2):
        print("=" * 40)
        print("Score|   {}: {}    {}: {}".format(player1.name, player1.score, player2.name, player2.score))
        print("=" * 40)

    @staticmethod
    def winner(player):
        if player is not None:
            print("{} wins!".format(player.name))
            player.win()
        else:
            print("Draw!")

    @staticmethod
    def is_valid_name(name):
        return name is not None and isinstance(name, str) and len(name) > 0
