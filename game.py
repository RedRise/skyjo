import uuid
from enum import Enum
from board import Board
from player import Player
from discard_pile import DiscardPile


class EventType(Enum):
    NEW_GAME = "NEW_GAME"
    NEW_ROUND = "NEW_ROUND"
    NEW_PLAYER_TURN = "NEW_PLAYER_TURN"
    PLAYER_DRAW = "PLAYER_DRAW"
    PLAYER_DRAW_DISCARD = "PLAYER_DRAW_DISCARD"
    PLAYER_REPLACE = "PLAYER_REPLACE"
    PLAYER_REVEAL = "PLAYER_REVEAL"


class Event:

    event_type: EventType
    comment: str
    data: dict

    def __init__(self, event_type: EventType, comment: str, data: dict):
        self.event_type = event_type
        self.comment = comment
        self.data = data


class Game:

    name: str
    uuid: uuid.UUID
    board: Board
    current_turn: int = -1
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

    def reveal_first_cards(self):
        for player in self.players:
            player.reveal_first_cards(self.board)

    def run(self):
        self.reveal_first_cards()

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

    def debug(self, events_to_watch: list[EventType]) -> list[Event]:
        self.reveal_first_cards()

        while True:
            if self.remaining_plays == 0:
                break

            for player in self.players:
                if self.remaining_plays == 0:
                    break

                yield Event(
                    EventType.NEW_PLAYER_TURN, f"New turn for {player.name}", {}
                )

                self.current_turn += 1

                player.take_turn(self.board)

                if self.remaining_plays:
                    self.remaining_plays -= 1
                else:
                    if player.playerBoard.check_end():
                        self.remaining_plays = len(self.players) - 1
