from player_board import NB_ROWS
from player import Player
from board import Board


def input_to_index(nb_cards: int) -> int:
    index = -1
    while index < 0 or index >= nb_cards:
        val = input()
        if len(val) == 2:
            index = (int(ord(val[0].lower())) - 97) * NB_ROWS + (int(val[1]) - 1)
    return index


def input_to_bool() -> bool:
    valid = False
    while not valid:
        val = input()
        if val == "y" or val == "n":
            valid = True
    return val == "y"


class PlayerTerm(Player):
    def __init__(self, name):
        super().__init__(name)

    def reveal_first_cards(self, board: Board):
        count_revealed = 0
        while count_revealed < 2:
            self.view()
            print("Select a card to reveal:")
            card_index = input_to_index(len(self.playerBoard.cards))

            boardCard = self.playerBoard.cards[card_index]
            if boardCard.revealed:
                print("This card is already revealed.")
            else:
                boardCard.revealed = True
                count_revealed += 1

    def want_to_draw(self, board: Board) -> bool:
        self.view()
        print(
            f"Do you want to keep this card (top discard) ? {board.discard_pile.peek()} (y/n)"
        )
        return not input_to_bool()

    def what_to_replace(self, card: int, board: Board) -> int:
        self.view()
        print(f"Do you want to replace a card with this one {card}? (y/n)")
        if input_to_bool():
            print("Select a card to replace:")
            return input_to_index(len(self.playerBoard.cards))
        return -1

    def what_to_reveal(self, board: Board) -> int:
        self.view()
        print("Select a card to reveal:")
        valid = False
        while not valid:
            index = input_to_index(len(self.playerBoard.cards))
            if not self.playerBoard.cards[index].revealed:
                valid = True
            else:
                print("This card is already revealed.")
        return index
