from abc import ABC, abstractmethod
from typing import List
from discard_pile import DiscardPile
from board import Board, PlayerBoard, BoardCard


class Player(ABC):

    playerBoard: PlayerBoard

    def __init__(self, name):
        self.name = name
        self.playerBoard = PlayerBoard(name)

    def __repr__(self):
        return f"Player {self.name}"

    def __len__(self):
        return len(self.cards)

    def initialize(self, deck):
        self.playerBoard.initialize(deck)

    def view(self):
        print(self.name)
        self.playerBoard.view()

    @abstractmethod
    def reveal_first_cards(self):
        """
        First step, reveal the first 2 cards of your board.
        """
        pass

    @abstractmethod
    def want_to_draw(self, board: Board) -> bool:
        """
        Return True if you want to draw a card from the deck, False if you want
        to draw from the discard pile.
        """
        pass

    @abstractmethod
    def what_to_replace(self, card: int) -> int:
        """
        Return the index of the card you want to replace, or -1 if you don't want
        """
        pass

    @abstractmethod
    def what_to_reveal(self) -> int:
        """
        Return the index of the card you want to reveal
        """
        pass

    def reveal_one(self):
        """
        Reveal one card from your board.
        """

        reveal_index: int = self.what_to_reveal()
        if self.playerBoard.cards[reveal_index].revealed:
            raise ValueError("Card already revealed")

        self.playerBoard.cards[reveal_index].revealed = True

    def replace_card(self, index: int, card: int, discard_pile: DiscardPile):
        """
        Replace a card from your board with a new one.
        """

        boardCard = self.cards[index]
        discard_pile.add(boardCard.value)
        self.playerBoard.cards[index] = BoardCard(card, revealed=True)

    def take_turn(self, board: Board):
        if not self.playerBoard.cards:
            raise ValueError("Player not initialized")

        card: int
        if self.want_to_draw(board):
            card = board.draw()
        else:
            card = board.discard_pile.draw()

        replace_index: int = self.what_to_replace(card)

        if replace_index < 0:
            self.reveal_one()
            board.discard_pile.add(card)
        else:
            self.replace_card(replace_index, card, board.discard_pile)

        # remove column if possible
        for col in range(self.playerBoard.max_col_idx, -1, -1):
            if self.playerBoard.check_column(col):
                self.playerBoard.remove_column(col)

        self.playerBoard.remove_columns()
