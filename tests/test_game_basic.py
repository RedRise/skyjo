from game import Game
from player_reveal import PlayerReveal
from player_term import PlayerTerm


def test_game_reveal():
    game = Game("Test", [PlayerReveal("Bob"), PlayerReveal("Alice")])
    game.play()

    assert game.remaining_plays == 0
    assert game.players[0].check_end()
    assert game.players[1].check_end()


def test_game_basic():
    game = Game("Test", [PlayerTerm("Bob"), PlayerTerm("Alice")])
    game.initialize()
    game.play()
