from typing import List
from player import Player
from deck import Deck
from discard_pile import DiscardPile


class Board:
    deck: Deck
    discard_pile: DiscardPile
    players: list[Player]
