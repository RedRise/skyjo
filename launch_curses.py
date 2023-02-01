import curses
from game import Game
from players.player_reveal import PlayerReveal
from players.player_term import PlayerTerm
from player_board import PlayerBoard, NB_ROWS, NB_COLS

screen = curses.initscr()
screen.border("|", "|", "-", "-", "+", "+", "+", "+")
screen.addstr(0, 0, "Welcome to the game!")
screen.refresh()

game = Game("Test", [PlayerReveal("Bob"), PlayerReveal("Alice")])
game.initialize()
# game.play()

bob = game.players[0]
alice = game.players[1]

pb = alice.playerBoard


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


for i, player in enumerate(game.players):
    window = player_board_to_window(player.playerBoard)
    window.mvwin(8, 2 + i * 20)
    window.refresh()

# deck
deck_window = curses.newwin(4, 10, 2, 2)
deck_window.border("|", "|", "-", "-", "+", "+", "+", "+")
deck_window.addstr(0, 0, "Deck")
deck_window.addstr(2, 2, f"#{str(len(game.board.deck))}")
deck_window.refresh()

# discard
discard_window = curses.newwin(4, 10, 2, 14)
discard_window.border("|", "|", "-", "-", "+", "+", "+", "+")
discard_window.addstr(0, 0, "Discard")
discard_window.addstr(2, 2, str(game.board.discard_pile.peek()))
discard_window.refresh()

screen.getstr()

curses.endwin()
