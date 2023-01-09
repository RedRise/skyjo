import uuid
from deck import Deck
from player import Player
from discard_pile import DiscardPile


class Game:

    name: str
    uuid: uuid.UUID
    players: list[Player]
    current_turn: int
    remaining_plays: int = None
    discard_pile: DiscardPile = None

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

        for player in self.players:
            player.first_reveal()

        self.current_turn = 0
        self.remaining_plays = None

    def __repr__(self):
        return f"Game({self.name!r}, {self.players!r}, turn={self.current_turn!r}"

    def shuffle_discard_pile(self):

        self.deck.cards.extend(self.discard_pile.cards)
        self.discard_pile.cards = []
        self.deck.shuffle()

    def draw(self):
        if len(self.deck) == 0:
            self.shuffle_discard_pile()

        return self.deck.draw()

    def play(self):
        while True:
            if self.remaining_plays == 0:
                break

            for player in self.players:
                if self.remaining_plays == 0:
                    break

                self.current_turn += 1
                print(f"Turn {self.current_turn}")

                player.take_turn(self.discard_pile, self.deck)

                if self.remaining_plays:
                    self.remaining_plays -= 1
                else:
                    if player.check_end():
                        self.remaining_plays = len(self.players) - 1
