import random
from .card import Card
from utils import SUITS, RANKS

class Deck:
    def __init__(self):
        self.deck_cards = []
        self.build_deck()

    def build_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck_cards.append(card)

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal(self):
        if not self.deck_cards:
            raise ValueError("No more cards to draw")
        return self.deck_cards.pop()