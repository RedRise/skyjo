from typing import List


class DiscardPile:

    cards: List[int] = None

    def __init__(self):
        self.cards = []

    def add(self, card: int):
        self.cards.append(card)

    def draw(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"DiscardPile: {len(self)}"
