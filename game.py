import uuid
from deck import Deck
from discard_pile import DiscardPile


class Game:
    def __init__(self, name):
        self.name = name
        self.uuid = uuid.uuid4()
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def initialize(self):
        deck = Deck()
        deck.shuffle()

        for player in self.players:
            player.initialize(deck)

        self.discard_pile = DiscardPile()
        self.discard_pile.add(deck.draw())
        self.deck = deck

        self.last_turn = False
        self.remaining_plays = None

    # def play(self):
    #     while True:
    #         for player in self.players:
    #             player.take_turn(self.deck, self.discard_pile)

    #             if player.check_end():
    #               self.set_end()

    #             if self.check_end():
    #                 return self.get_winner()

    def __repr__(self):
        return f"Game({self.name!r}, {self.players!r})"
