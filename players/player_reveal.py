from player import Player
from board import Board


class PlayerReveal(Player):
    def __init__(self, name):
        super().__init__(name)

    def reveal_first_cards(self, board: Board):
        for i in range(2):
            self.playerBoard.cards[i].revealed = True

    def want_to_draw(self, board: Board) -> bool:
        return True

    def what_to_replace(self, card: int, board: Board) -> int:
        return -1

    def what_to_reveal(self, board: Board) -> int:
        for i, card in enumerate(self.playerBoard.cards):
            if not card.revealed:
                return i
