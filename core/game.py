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
    
    def hit_or_stand(self):
        while True:
            choice = input("Deseja comprar uma carta ou parar? [H/S] ").upper()

            if choice == "H":
                self.player_hand.add_card(self.deck.deal())
                print(self.player_hand.hand_cards)
                print(self.player_hand.hand_value)

                if self.player_hand.hand_value > 21:
                    print("BUST! Hand value greater than 21.")
                    self.player_chips.lose_bet()
                    return False

            elif choice == "S":
                print("You chose to keep your cards.")
                return True

            else: 
                print("Comando inválido")

    def dealer_turn(self):
        while self.dealer_hand.hand_value < 17:
            self.dealer_hand.add_card(self.deck.deal())
            print(self.dealer_hand.hand_cards)
            print(self.dealer_hand.hand_value)

        if self.dealer_hand.hand_value > 21:
            print("Dealer BUST! Player wins.")
            self.player_chips.win_bet()
            return False
        
        return True
            
    def compare_hands(self):
        if self.player_hand.hand_value > self.dealer_hand.hand_value:
            print("Player wins! Higher hand value.")
            self.player_chips.win_bet()
            return True
        elif self.player_hand.hand_value < self.dealer_hand.hand_value:
            print("Player loses! Dealer with higher hand value.")
            self.player_chips.lose_bet()
            return False
        else: 
            print("Push! Same hand value for both.")
            return 

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
                player_survived = self.hit_or_stand()
                
                if player_survived:
                    ## Aqui entrará o loop do Dealer (se o jogador não estourar).
                    dealer_survived = self.dealer_turn()
                    if dealer_survived:
                        ## Aqui entrará a comparação final de quem ganhou.
                        self.compare_hands()

            if self.player_chips.total <= 0:
                print("No more chips!")
                break

            while True:
                keep_playing = input(f"Seu saldo é {self.player_chips.total}. Deseja jogar mais uma rodada? [S/N] ").upper()

                if keep_playing == "S":
                    break
                elif keep_playing == "N":
                    print("Thank you for playing!")
                    return 
                else:
                    print("Invalid input!")

 






