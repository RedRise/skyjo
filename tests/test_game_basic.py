from game import Game
from players.player_reveal import PlayerReveal


def test_game_reveal():
    game = Game("Test", [PlayerReveal("Bob"), PlayerReveal("Alice")])
    game.play()

    assert game.remaining_plays == 0
    assert game.players[0].playerBoard.check_end()
    assert game.players[1].playerBoard.check_end()
