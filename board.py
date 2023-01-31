from typing import List
from deck import Deck
from player_board import PlayerBoard, BoardCard
from discard_pile import DiscardPile


class Board:

    deck: Deck
    discard_pile: DiscardPile
    players: list[PlayerBoard]

    def __init__(self, players: List[PlayerBoard]):
        self.players = players

        self.deck = Deck()
        self.deck.shuffle()

        for player in self.players:
            player.initialize(self.deck)

        self.discard_pile = DiscardPile()
        self.discard_pile.add(self.deck.draw())

    def shuffle_discard_pile(self):
        self.deck.cards.extend(self.discard_pile.cards)
        self.discard_pile.cards = []
        self.deck.shuffle()

    def draw(self):
        if len(self.deck) == 0:
            self.shuffle_discard_pile()

        return self.deck.draw()
