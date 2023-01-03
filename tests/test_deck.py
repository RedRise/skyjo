from deck import Deck


def test_deck():
    deck = Deck()
    assert deck


def test_deck_length():
    deck = Deck()
    assert len(deck) == 140


def test_deck_pop():
    deck = Deck()
    card = deck.cards.pop()
    assert card == 12


def test_deck_shuffle():
    deck = Deck()
    deck.shuffle()

    deck_benchmark = Deck()

    diff_list = []
    while len(deck) > 0:
        card = deck.cards.pop()
        card_benchmark = deck_benchmark.cards.pop()
        diff_list.append(card != card_benchmark)

    assert any(diff_list)
