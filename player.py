from typing import List

NB_ROWS = 3
NB_COLS = 4


class Player:

    cards: List[int] = None
    revealed: List[int] = None
    columns: int

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Player {self.name}"

    def initialize(self, deck):
        if len(deck) < NB_ROWS * NB_COLS:
            raise ValueError("Not enough cards in deck")

        if self.cards:
            raise ValueError("Player already initialized")

        self.cards = []
        for _ in range(NB_ROWS * NB_COLS):
            self.cards.append(deck.cards.pop())

        self.revealed = [False] * NB_ROWS * NB_COLS

        self.columns = NB_COLS - 1

    def get_column(self, column: int):
        if column > self.columns or column < 0:
            raise ValueError("Column does not exist")

        return self.cards[column * NB_ROWS : (column + 1) * NB_ROWS]

    def view(self):
        print(self.name)
        for i in range(NB_ROWS):
            row = []
            for j in range(self.columns + 1):
                if self.revealed[i + j * NB_ROWS]:
                    row.append("{:2d}".format(self.cards[i + j * NB_ROWS]))
                else:
                    row.append("XX")
            print(" ".join(row))

    def check_column(self, column: int):
        if column > self.columns or column < 0:
            raise ValueError("Column does not exist")

        column = self.get_column(column)
        return all([x == column[0] for x in column[1:]])

    def remove_column(self, column: int):
        if column > self.columns or column < 0:
            raise ValueError("Column does not exist")

        self.cards = (
            self.cards[: column * NB_ROWS] + self.cards[(column + 1) * NB_ROWS :]
        )
        self.columns -= 1


# from deck import Deck
# deck = Deck()
# deck.shuffle()
# player = Player("Bob")
# player.initialize(deck)
# player.get_column(0)
# player.get_column(3)
# player.view()
# player.revealed[10] = True

# player.check_column(0)
# player.remove_column(0)
# player.columns
