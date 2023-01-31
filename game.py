import uuid
from board import Board
from deck import Deck
from player import Player
from discard_pile import DiscardPile


class Game:

    name: str
    uuid: uuid.UUID
    board: Board
    # players: list[Player]
    current_turn: int
    remaining_plays: int = None
    discard_pile: DiscardPile = None

    @property
    def players(self) -> list[Player]:
        return self.board.players

    def __init__(self, name: str, players: list[Player]):
        self.name = name
        self.uuid = uuid.uuid4()
        self.board = Board(players)

    def initialize(self):
        self.current_turn = 0
        self.remaining_plays = None

    def __repr__(self):
        return f"Game({self.name!r}, {self.players!r}, turn={self.current_turn!r}"

    def play(self):
        while True:
            if self.remaining_plays == 0:
                break

            for player in self.players:
                if self.remaining_plays == 0:
                    break

                self.current_turn += 1
                print(f"Turn {self.current_turn}")

                player.take_turn(self.board)

                if self.remaining_plays:
                    self.remaining_plays -= 1
                else:
                    if player.playerBoard.check_end():
                        self.remaining_plays = len(self.players) - 1
