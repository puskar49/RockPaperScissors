from menu import Menu
from player import CPU, Human


class Game(object):
    @staticmethod
    def run():
        menu = Menu()
        cpu = CPU()
        human = Human(menu.greet())
        while menu.play:
            human_throw = human.throw()
            menu.announce(human, human_throw)
            cpu_throw = cpu.throw()
            menu.announce(cpu, cpu_throw)
            if human_throw > cpu_throw:
                menu.winner(human)
            elif cpu_throw > human_throw:
                menu.winner(cpu)
            else:
                menu.winner(None)
            menu.score(human, cpu)
            menu.end_round()


if __name__ == "__main__":
    game = Game()
    game.run()
