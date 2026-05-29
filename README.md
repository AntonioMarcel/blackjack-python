# Python Terminal Blackjack

A fully functional, Object-Oriented command-line Blackjack game written in Python. This project simulates a real casino experience right in your terminal, complete with betting systems, dealer logic, and strict casino rules.

## Features

* **Object-Oriented Design:** Clean and modular architecture using separate classes for Cards, Decks, Hands, Chips, and the main Game logic.
* **Betting System:** Players start with a chip balance and place bets each round. Payouts and losses are handled automatically.
* **Casino Rules Enforcement:** * Dealer is programmed to hit until they reach 17.
  * Natural Blackjack (21 on the first two cards) detection.
  * "Push" (Tie) handling where the bet is safely returned to the player.
* **Dynamic Ace Valuation:** Aces automatically adjust their value (11 or 1) to prevent the player or dealer from busting.
* **Immersive Terminal UI:** Visual feedback showing hidden cards (hole cards), dramatic reveals, and turn-by-turn action logs.

## Project Structure

The codebase is split into modular components for easy maintenance and scalability:

* `Card`: Represents a single playing card with a specific suit and rank.
* `Deck`: Represents a standard 52-card deck. Handles generation, shuffling, and dealing.
* `Hand`: Manages the cards held by a player/dealer, calculates the total hand value, and manages Ace adjustments.
* `Chips`: Manages the player's bankroll, validating funds and handling betting transactions.
* `Game`: The core engine that ties all objects together, managing the game loop, user inputs, and winning/losing conditions.

## How to Run

1. Ensure you have **Python 3.x** installed on your machine.
2. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   ```
3. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```
4. Run the game:
   ```bash
   python main.py
   ```
   *(Note: Ensure you are running the entry-point file where the `Game` class is instantiated).*

## How to Play

1. **Place your bet:** Enter the amount of chips you wish to wager at the start of the round.
2. **Analyze the table:** You will receive two cards face up. The dealer receives one card face up and one hidden.
3. **Hit or Stand:** * Type `H` to **Hit** (take another card) to get your total closer to 21.
   * Type `S` to **Stand** (keep your hand) and pass the turn to the dealer.
4. **Winning Conditions:** You win if your hand's total is higher than the dealer's without exceeding 21, or if the dealer busts (goes over 21). If your hand exceeds 21, you bust and lose your bet instantly.