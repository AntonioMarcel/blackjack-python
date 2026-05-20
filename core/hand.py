from .card import Card

class Hand:
    def __init__(self):
        self.hand_cards = []
        self.hand_value = 0
        self.num_aces = 0

    def add_card(self, card: Card):
        self.hand_cards.append(card)
        self.hand_value += card.get_value()

        if card.rank == 'A':
            self.num_aces += 1

        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.hand_value > 21 and self.num_aces > 0:
                self.hand_value -= 10
                self.num_aces -= 1




    