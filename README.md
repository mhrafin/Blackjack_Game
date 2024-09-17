# Blackjack_Game
This is a simple command-line implementation of the popular card game Blackjack, written in Python.

## How to Play
1.  The game begins with two cards dealt to both the player and the dealer.
2.  The player can see both of their cards but only one of the dealer's cards.
3.  The player decides whether to draw another card or stay.
4.  The dealer must continue drawing cards until their total is 17 or higher.
5.  The game determines the winner based on whose hand is closest to 21 without exceeding it.


## Features
-   Simple text-based Blackjack gameplay.
-   Handles Ace cards, allowing players to choose whether it counts as 1 or 11.
-   Dealer automatically draws cards according to Blackjack rules.
-   Option to play multiple rounds.
-   Cross-platform support (clears the terminal screen on both Windows and Linux/MacOS).


## Installation
1. Clone the repository:
```git clone https://github.com/mhrafin/Blackjack_Game.git```
2. Navigate to the project folder:
```cd Blackjack_Game```
3. Run the game:
```python blackjack.py```


## Game Rules
-   Face cards (King, Queen, Jack) are worth 10 points.
-   Aces can be worth 1 or 11 points, depending on the player's choice.
-   The player must decide whether to draw another card or stay with their current hand.
-   If the player's total exceeds 21, they lose.
-   If the dealer’s hand exceeds 21, the player wins.
-   If neither hand exceeds 21, the hand closest to 21 wins.
