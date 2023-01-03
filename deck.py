from typing import List
import random


class Deck:

    cards: List[int]

    def __init__(self) -> None:
        self.cards = []
        for i in range(-2, 0):
            for _ in range(5):
                self.cards.append(i)

        for _ in range(10):
            self.cards.append(0)

        for i in range(1, 13):
            for _ in range(10):
                self.cards.append(i)

    def __len__(self):
        return len(self.cards)

    def __repr__(self) -> str:
        return f"Deck: {len(self)}"

    def shuffle(self):
        random.shuffle(self.cards)
