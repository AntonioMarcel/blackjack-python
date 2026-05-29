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

    def clear_hand(self):
         self.hand_cards.clear()
         self.hand_value = 0
         self.num_aces = 0

    def __str__(self):
        txt = f"Valor total: {self.hand_value}\nCartas:"

        for card in self.hand_cards:
             txt += f"\n - {card}"

        return txt




    