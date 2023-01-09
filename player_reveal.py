from player import Player


class PlayerReveal(Player):
    def __init__(self, name):
        super().__init__(name)

    def first_reveal(self):
        for i in range(2):
            self.cards[i].revealed = True

    def prefer_to_draw(self, top_discard_card: int) -> bool:
        return True

    def check_for_replace(self, card: int) -> int:
        return -1

    def choose_to_reveal(self) -> int:
        for i, card in enumerate(self.cards):
            if not card.revealed:
                return i
