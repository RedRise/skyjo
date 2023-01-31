from game import Game
from players.player_reveal import PlayerReveal
from players.player_term import PlayerTerm

game = Game("Test", [PlayerReveal("Bob"), PlayerTerm("Alice")])
game.initialize()
game.play()
