from player_reveal import PlayerReveal
from deck import Deck
import pytest


@pytest.fixture
def deck():
    deck = Deck()
    deck.shuffle()
    return deck


def test_player_name():
    player = PlayerReveal("Bob")
    assert player.name == "Bob"


def test_player_repr():
    player = PlayerReveal("Bob")
    assert repr(player) == "Player Bob"
