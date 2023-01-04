from player import Player, NB_ROWS, NB_COLS
from deck import Deck
import pytest


@pytest.fixture
def deck():
    deck = Deck()
    deck.shuffle()
    return deck


def test_player():
    player = Player("Bob")
    assert player


def test_player_name():
    player = Player("Bob")
    assert player.name == "Bob"


def test_player_repr():
    player = Player("Bob")
    assert repr(player) == "Player Bob"


def test_player_initialize(deck):
    player = Player("Bob")
    player.initialize(deck)
    assert player.cards


def test_player_initialize_not_enough_cards(deck):
    player = Player("Bob")
    deck.cards = deck.cards[:10]
    with pytest.raises(ValueError):
        player.initialize(deck)


def test_player_initialize_already_initialized(deck):
    player = Player("Bob")
    player.initialize(deck)
    with pytest.raises(ValueError):
        player.initialize(deck)


def test_player_get_column(deck):
    player = Player("Bob")
    player.initialize(deck)
    column = player.get_column(0)
    assert len(column) == NB_ROWS


def test_player_check_column(deck):
    player = Player("Bob")
    player.initialize(deck)
    for i in range(NB_ROWS):
        player.cards[i].revealed = True
        player.cards[i].value = 0
    assert player.check_column(0)


def test_player_remove_column(deck):
    player = Player("Bob")
    player.initialize(deck)
    player.remove_column(0)
    assert len(player.cards) == NB_ROWS * (NB_COLS - 1)
    assert player.max_col_idx == NB_COLS - 2
