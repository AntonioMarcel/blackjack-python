class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            # Aces can be worth 11 or 1, but we'll start with 11 and adjust later if needed
            return 11 
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"