import curses
from curses import wrapper
from typing import Dict
from game import Game
from players.player_reveal import PlayerReveal
from player_board import PlayerBoard, NB_ROWS, NB_COLS


def player_board_to_window(pb: PlayerBoard):
    pb_window = curses.newwin(5 + NB_ROWS, 4 + 3 * NB_COLS, 8, 2)
    pb_window.border("|", "|", "-", "-", "+", "+", "+", "+")
    pb_window.addstr(0, 0, f"{pb.name}")
    for i in range(NB_ROWS):
        row = []
        for j in range(pb.max_col_idx + 1):
            row.append(str(pb.cards[i + j * NB_ROWS]))
        pb_window.addstr(4 + i, 4, " ".join(row))
    for j in range(NB_COLS):
        pb_window.addstr(2, 1 + 4 + 3 * j, chr(97 + j))
    for i in range(NB_ROWS):
        pb_window.addstr(4 + i, 1, str(i + 1))

    return pb_window


def deck_to_window(deck):
    deck_window = curses.newwin(4, 10, 2, 2)
    deck_window.border("|", "|", "-", "-", "+", "+", "+", "+")
    deck_window.addstr(0, 0, "Deck")
    deck_window.addstr(2, 2, f"#{str(len(deck))}")
    return deck_window


def discard_to_window(discard):
    discard_window = curses.newwin(4, 10, 2, 14)
    discard_window.border("|", "|", "-", "-", "+", "+", "+", "+")
    discard_window.addstr(0, 0, "Discard")
    discard_window.addstr(2, 2, str(discard.peek()))
    return discard_window


class CursesUI:

    height: int
    width: int
    # screen
    # deck: curses._CursesWindow
    # discard: curses._CursesWindow
    # players: Dict[str, curses._CursesWindow] = {}

    def __init__(self):
        self.screen = curses.initscr()
        self.height, self.width = self.screen.getmaxyx()
        self.players = {}

    def update_maxyx(self):
        self.height, self.width = self.screen.getmaxyx()

    def draw_deck(self, deck):
        self.deck = deck_to_window(deck)
        self.deck.refresh()

    def draw_discard(self, discard):
        self.discard = discard_to_window(discard)
        self.discard.refresh()

    def draw_player_boards(self, game: Game):
        for i, player in enumerate(game.players):
            player_win = player_board_to_window(player.playerBoard)
            player_win.mvwin(8, 2 + i * 20)
            player_win.refresh()
            self.players[player.name] = player_win

    def clear_all(self):
        self.screen.clear()
        self.deck.clear()
        self.discard.clear()
        for player in self.players.values():
            player.clear()

    def resize(self):
        self.update_maxyx()
        # self.clear_all()

    def cdraw_prompt(self, prompt):
        self.screen.addstr(self.height - 1, 0, prompt)


def get_game():
    return Game(
        "Test", [PlayerReveal("Bob"), PlayerReveal("Alice"), PlayerReveal("Charlie")]
    )


def main(stdscr):
    # Clear screen
    stdscr.clear()

    game = get_game()
    game.initialize()

    cui = CursesUI()

    should_quit = False

    for _ in game.debug([]):
        while True:
            cui.screen.clear()
            cui.screen.refresh()

            cui.draw_deck(game.board.deck)
            cui.draw_discard(game.board.discard_pile)
            cui.draw_player_boards(game)

            cui.draw_prompt("Press c to continue / q to quit")
            # cui.screen.refresh()

            c = stdscr.getch()
            if c == ord("q"):
                should_quit = True
                break
            elif c == ord("c"):
                break
            elif c == curses.KEY_RESIZE:
                cui.resize()
                pass

        if should_quit:
            break


wrapper(main)
