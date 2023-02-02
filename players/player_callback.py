from collections.abc import Callable
from typing import List
from player_board import NB_ROWS
from player import Player
from board import Board


def control_choice(actions: List[int], choice: int) -> bool:
    return choice in actions


class PlayerCallback(Player):
    def __init__(self, name, action_selector: Callable[[str, List[int]], int]):
        super().__init__(name)
        self.action_selector = action_selector

    def select_a_card_to_reveal(self) -> int:
        valid_action = False
        while not valid_action:
            prompt = "Select a card to reveal"
            actions = [
                i for i, card in enumerate(self.playerBoard.cards) if not card.revealed
            ]
            card_index = self.action_selector(prompt, actions)
            valid_action = control_choice(actions, card_index)

        return card_index

    def reveal_first_cards(self, board: Board):
        count_revealed = 0

        while count_revealed < 2:
            card_index = self.select_a_card_to_reveal()
            boardCard = self.playerBoard.cards[card_index]
            boardCard.revealed = True
            count_revealed += 1

    def want_to_draw(self, board: Board) -> bool:
        self.view()
        print(
            f"Do you want to keep this card (top discard) ? {board.discard_pile.peek()} (y/n)"
        )
        return True  # not input_to_bool()

    def what_to_replace(self, card: int, board: Board) -> int:
        self.view()
        print(f"Do you want to replace a card with this one {card}? (y/n)")
        if True:  # input_to_bool():
            print("Select a card to replace:")
            return 0  # input_to_index(len(self.playerBoard.cards))
        return -1

    def what_to_reveal(self, board: Board) -> int:
        self.view()
        print("Select a card to reveal:")
        valid = False
        while not valid:
            index = 0  # input_to_index(len(self.playerBoard.cards))
            if not self.playerBoard.cards[index].revealed:
                valid = True
            else:
                print("This card is already revealed.")
        return index
