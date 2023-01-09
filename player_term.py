from player import Player, NB_ROWS


def input_to_index(nb_cards: int) -> int:
    index = -1
    while index < 0 or index > nb_cards:
        val = input()
        if len(val) == 2:
            index = (int(ord(val[0].lower())) - 97) * NB_ROWS + (int(val[1]) - 1)
    return index


class PlayerTerm(Player):
    def __init__(self, name):
        super().__init__(name)

    def first_reveal(self):
        for i in range(2):
            self.view()
            print("Select a card to reveal:")
            card_index = input_to_index(len(self.cards))
            self.cards[card_index].revealed = True

    def prefer_to_draw(self, top_discard_card: int) -> bool:
        self.view()
        print(f"Do you want to keep this card (top discard) ? {top_discard_card} (y/n)")
        return input() != "y"

    def check_for_replace(self, card: int) -> int:
        self.view()
        print(f"Do you want to replace a card with this one {card}? (y/n)")
        if input() == "y":
            print("Select a card to replace:")
            return input_to_index(len(self.cards))
        return -1

    def choose_to_reveal(self) -> int:
        self.view()
        print("Select a card to reveal:")
        return input_to_index(len(self.cards))
