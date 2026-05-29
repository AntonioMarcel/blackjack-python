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
                bet = int(input("Enter your bet amount: "))
            except ValueError:
                print("The bet amount must be a number.")
                continue

            if bet > self.player_chips.total:
                print("Insufficient funds (bet amount > available chips).")
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
            self.show_all()
            print("Push! Natural Blackjack for both.")
            print("-"*30)
            return
        elif self.player_hand.hand_value == 21:
            self.show_all()
            print("Natural Blackjack! Player wins.")
            print("-"*30)
            self.player_chips.win_bet()
            return True
        elif self.dealer_hand.hand_value == 21:
            self.show_all()
            print("Dealers' Natural Blackjack! Player loses.")
            print("-"*30)
            self.player_chips.lose_bet()
            return True
        
        return False
    
    def hit_or_stand(self):
        while True:
            choice = input("Would you like to Hit or Stand? [H/S] ").upper()

            if choice == "H":
                self.player_hand.add_card(self.deck.deal())
                print("-"*30)
                print(f"Player - {self.player_hand}")
                print("-"*30)

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
        print("------- Dealer's turn -------")
        self.show_all()

        while self.dealer_hand.hand_value < 17:
            self.dealer_hand.add_card(self.deck.deal())
            print(f"Dealer - {self.dealer_hand}")
            print("-"*30)

        if self.dealer_hand.hand_value > 21:
            print("Dealer BUST! Player wins.")
            self.player_chips.win_bet()
            return False
        
        return True
            
    def compare_hands(self):
        print("="*30)
        print("FINAL RESULT")
        print("="*30)
        if self.player_hand.hand_value > self.dealer_hand.hand_value:
            print("Player wins! Higher hand value.")
            self.player_chips.win_bet()
            return True
        elif self.player_hand.hand_value < self.dealer_hand.hand_value:
            print("Player loses! Dealer with higher hand value.")
            self.player_chips.lose_bet()
            return False
        else: 
            print("Push! Same hand value for both!")
            return 
        
    def show_some(self):
        print("="*30)
        print("STARTING HANDS")
        print("="*30)
        print("Dealer shows:")
        print("[Hidden Card]")
        print(f" - {self.dealer_hand.hand_cards[1]}")
        print("-"*30)
        print("Player Cards:")
        print(self.player_hand)

    def show_all(self):
            print("="*30)
            print("HANDS REVEALED")
            print("="*30)
            print(f"Dealer's Hand:\n{self.dealer_hand}")
            print("-"*30)
            print(f"Player Cards:\n{self.player_hand}")
            print("="*30)

    def play_game(self):
        while True:
            print("#"*40)
            print("WELCOME TO A NEW ROUND OF BLACKJACK!!")
            print("#"*40)            
            
            self.player_hand.clear_hand()
            self.dealer_hand.clear_hand()

            self.take_bet()
            self.deal_initial_cards()

            self.show_some()

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
                print("No more chips! Game over!")
                break

            while True:
                keep_playing = input(f"Your current balance is {self.player_chips.total}. Would you like to play another round? [Y/N] ").upper()

                if keep_playing == "Y":
                    break
                elif keep_playing == "N":
                    print("Thank you for playing!")
                    return 
                else:
                    print("Invalid input!")

 






