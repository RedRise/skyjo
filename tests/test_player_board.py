from player_board import PlayerBoard, NB_ROWS, NB_COLS
from deck import Deck
import pytest


@pytest.fixture
def deck():
    deck = Deck()
    deck.shuffle()
    return deck


def test_playerboard_name():
    player = PlayerBoard("Bob")
    assert player.name == "Bob"


def test_playerboard_initialize(deck):
    player = PlayerBoard("Bob")
    player.initialize(deck)
    assert True  # player.cards


def test_playerboard_initialize_not_enough_cards(deck):
    player = PlayerBoard("Bob")
    deck.cards = deck.cards[:10]
    with pytest.raises(ValueError):
        player.initialize(deck)


def test_playerboard_initialize_already_initialized(deck):
    player = PlayerBoard("Bob")
    player.initialize(deck)
    with pytest.raises(ValueError):
        player.initialize(deck)


def test_playerboard_get_column(deck):
    player = PlayerBoard("Bob")
    player.initialize(deck)
    column = player.get_column(0)
    assert len(column) == NB_ROWS


def test_playerboard_check_column(deck):
    player = PlayerBoard("Bob")
    player.initialize(deck)
    for i in range(NB_ROWS):
        player.cards[i].revealed = True
        player.cards[i].value = 0
    assert player.check_column(0)


def test_playerboard_remove_column(deck):
    player = PlayerBoard("Bob")
    player.initialize(deck)
    player.remove_column(0)
    assert len(player.cards) == NB_ROWS * (NB_COLS - 1)
    assert player.max_col_idx == NB_COLS - 2


def test_playerboard_check_end(deck):
    player = PlayerBoard("Bob")
    player.initialize(deck)
    assert not player.check_end()

    for i in range(len(player)):
        player.cards[i].revealed = True
    assert player.check_end()
