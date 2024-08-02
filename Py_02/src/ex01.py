from collections import Counter

step = {("+", "+"): (2, 2), ("+", "-"): (-1, 3),
        ("-", "+"): (3, -1), ("-", "-"): (0, 0)}
# cheat -
# coop +


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        player1.__init__()
        player2.__init__()
        for _ in range(self.matches):
            self.registry[player1.__class__.__name__] += step[(
                player1.decision(), player2.decision())][0]
            self.registry[player2.__class__.__name__] += step[(
                player1.decision(), player2.decision())][1]

            player1.history.append(player1.decision())
            player1.opponent = player2.history
            player2.history.append(player2.decision())
            player2.opponent = player1.history

    def top3(self):
        top3 = Counter(self.registry).most_common(3)
        for player, score in top3:
            print(player, score)


class Player(object):
    def __init__(self):
        self.history = []
        self.opponent = []

    def __del__(self):
        self.history.clear()
        self.opponent.clear()


class Cheater(Player):
    def decision(self):
        return '-'


class Cooperator(Player):
    def decision(self):
        return '+'


class Copycat(Player):
    def decision(self):
        if len(self.history) == 0:
            return '+'
        else:
            return self.opponent[len(self.history) - 1]


class Grudger(Player):
    def decision(self):
        if any(x == '-' for x in self.opponent[0:len(self.history)]):
            return '-'
        else:
            return '+'


class Detective(Player):
    def decision(self):
        if len(self.history) < 4:
            return ['+', '-', '+', '+'][len(self.history)]
        elif not any(x == '-' for x in self.opponent[0:4]):
            return '-'
        else:
            return self.opponent[len(self.history) - 1]


class Rudolf(Player):
    def decision(self):
        flag = ''
        if len(self.opponent) >= 1 and self.opponent[0] == '-':
            flag = 'cheater'
        elif len(self.opponent) >= 2 and self.opponent[0] == '+' and self.opponent[1] == '-':
            flag = 'detective'
        elif len(self.opponent) > 2 and self.opponent[0] == '+' and self.opponent[1] == '+':
            flag = 'cooperater'
        else:
            flag = ''
        if len(self.history) == 0:
            return '+'
        elif flag == 'cheater':
            return '-'
        elif flag == 'detective':
            return ['-', '-', '+', '-', '+', '-',
                    '+', '-'][len(self.history) - 2]
        elif flag == 'cooperater':
            return ['+', '+', '+', '+', '+', '+',
                    '+', '-'][len(self.history) - 2]
        else:
            return '+'
