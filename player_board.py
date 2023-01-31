from typing import List

NB_ROWS = 3
NB_COLS = 4


class BoardCard:
    value: int
    revealed: bool

    def __init__(self, value, revealed=False):
        self.value = value
        self.revealed = revealed

    def __repr__(self):
        return "{:2d}".format(self.value) if self.revealed else "XX"


class PlayerBoard:

    name: str = ""
    cards: List[BoardCard] = None
    max_col_idx: int

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Player {self.name}"

    def __len__(self):
        return len(self.cards)

    def initialize(self, deck):
        if len(deck) < NB_ROWS * NB_COLS:
            raise ValueError("Not enough cards in deck")

        if self.cards:
            raise ValueError("Player already initialized")

        self.cards = []
        for _ in range(NB_ROWS * NB_COLS):
            self.cards.append(BoardCard(deck.draw(), revealed=False))

        self.max_col_idx = NB_COLS - 1

    def get_column(self, column: int):
        if column > self.max_col_idx or column < 0:
            raise ValueError("Column does not exist")

        return self.cards[column * NB_ROWS : (column + 1) * NB_ROWS]

    def check_column(self, column: int):
        if column > self.max_col_idx or column < 0:
            raise ValueError("Column does not exist")

        column = self.get_column(column)

        return all([x.value == column[0].value for x in column[1:]]) and all(
            [x.revealed for x in column]
        )

    def view(self):
        print(self.name)
        for i in range(NB_ROWS):
            row = []
            for j in range(self.max_col_idx + 1):
                row.append(str(self.cards[i + j * NB_ROWS]))

            print(" ".join(row))

    def remove_column(self, column: int):
        """
        Remove a column from the player board.
        """
        if column > self.max_col_idx or column < 0:
            raise ValueError("Column does not exist")

        self.cards = (
            self.cards[: column * NB_ROWS] + self.cards[(column + 1) * NB_ROWS :]
        )
        self.max_col_idx -= 1

    def remove_columns(self):
        """
        Remove all columns that are required to be removed.
        """
        for col in range(self.max_col_idx, -1, -1):
            if self.check_column(col):
                self.remove_column(col)

    def check_end(self) -> bool:
        return all([x.revealed for x in self.cards])
