from player import Player
from board import Board


class PlayerReveal(Player):
    def __init__(self, name):
        super().__init__(name)

    def reveal_first_cards(self):
        for i in range(2):
            self.cards[i].revealed = True

    def want_to_draw(self, board: Board) -> bool:
        return True

    def what_to_replace(self, card: int) -> int:
        return -1

    def what_to_reveal(self) -> int:
        for i, card in enumerate(self.cards):
            if not card.revealed:
                return i
