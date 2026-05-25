from .chips import Chips
from .deck import Deck
from .hand import Hand

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_chips = Chips()

    def take_bet(self):
        while True:
            try:
                bet = int(input("Digite o valor de sua aposta: "))
            except ValueError:
                print("O valor da aposta deve ser um número.")
                continue

            if bet > self.player_chips.total:
                print("Não há saldo suficiente (total apostado > total disponível).")
            else:
                self.player_chips.bet = bet
                break

    def deal_initial_cards(self):
        self.deck.shuffle()
        
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def check_natural_blackjack(self):
        self.player_hand.hand_value = 21
        self.dealer_hand.hand_value = 21
        if self.player_hand.hand_value == self.dealer_hand.hand_value == 21:
            print("Push! Natural Blackjack for both.")
            return True
        elif self.player_hand.hand_value == 21:
            print("Natural Blackjack! Player wins.")
            self.player_chips.win_bet()
            return True
        elif self.dealer_hand.hand_value == 21:
            print("Dealers' Natural Blackjack! Player loses.")
            self.player_chips.lose_bet()
            return True
        
        return False

    def play_game(self):
        while True:
            self.player_hand.clear_hand()
            self.dealer_hand.clear_hand()

            self.take_bet()
            self.deal_initial_cards()
            natural_blackjack = self.check_natural_blackjack()

            if not natural_blackjack:
                # Próximos passos    
                ## Aqui entrará o loop de Hit or Stand do Jogador.
                ## Aqui entrará o loop do Dealer (se o jogador não estourar).
                ## Aqui entrará a comparação final de quem ganhou.
                pass

            if self.player_chips.total <= 0:
                print("No more chips!")
                break

            one_more = input(f"Seu saldo é {self.player_chips.total}. Deseja jogar mais uma rodada? S/N").upper()

            if one_more == "N":
                break
                    

 






