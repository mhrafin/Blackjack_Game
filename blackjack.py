import random
import sys
import os


def main():
    print(r"""
__________.__                 __          ____.              __    
\______   \  | _____    ____ |  | __     |    |____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /     |    \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    <  /\__|    |/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \ \________(____  /\___  >__|_ \
        \/          \/     \/     \/               \/     \/     \/
    """)
    cards_on_table = add_cards_to_hands()
    players_hand = cards_on_table["players_hand"]
    dealers_hand = cards_on_table["dealers_hand"]

    print(f"Your Hand: {players_hand}. Total: {sum(players_hand)}")
    print(f"Dealer's First Card: {dealers_hand[0]}")

    if sum(dealers_hand) > 21:
        print(
            f"Sum of Dealers hand is bigger than 21. {dealers_hand} =  {sum(dealers_hand)}"
        )
        print("You Win!\n")
        play_again = input(
            "Do want to play again?\nType 'y' for Yes or 'n' for No.\n"
        ).lower()
        if play_again == "y":
            os.system("cls" if os.name == "nt" else "clear")
            main()
        else:
            sys.exit(0)

    while sum(players_hand) <= 21:
        draw_another = input("Do you want to draw another? Yes(y) or No(n)\n")
        if draw_another == "y":
            players_hand.append(card(True))
            print()
            print(f"Your Hand: {players_hand}. Total: {sum(players_hand)}")
        else:
            print()
            break

    while sum(dealers_hand) < 17:
        dealers_hand.append(card(False))

    if sum(players_hand) > 21:
        print(
            f"Sum of Player's hand is bigger than 21. {players_hand} =  {sum(players_hand)}"
        )
        print("You Lost\n")
        play_again = input(
            "Do want to play again?\nType 'y' for Yes or 'n' for No.\n"
        ).lower()
        if play_again == "y":
            os.system("cls" if os.name == "nt" else "clear")
            main()
        else:
            sys.exit(0)
    if sum(dealers_hand) > 21:
        print(
            f"Sum of Dealers hand is bigger than 21. {dealers_hand} =  {sum(dealers_hand)}"
        )
        print("You Win!\n")
        play_again = input(
            "Do want to play again?\nType 'y' for Yes or 'n' for No.\n"
        ).lower()
        if play_again == "y":
            os.system("cls" if os.name == "nt" else "clear")
            main()
        else:
            sys.exit(0)

    if sum(players_hand) > sum(dealers_hand):
        print(f"Sum of Player's hand is bigger than Sum of Dealer's hand.")
        print(
            f"{players_hand} = {sum(players_hand)} > {dealers_hand} = {sum(dealers_hand)}"
        )
        print("You Win!\n")
        play_again = input(
            "Do want to play again?\nType 'y' for Yes or 'n' for No.\n"
        ).lower()
        if play_again == "y":
            os.system("cls" if os.name == "nt" else "clear")
            main()
        else:
            sys.exit(0)
    elif sum(players_hand) < sum(dealers_hand):
        print(f"Sum of Player's hand is lower than Sum of Dealer's hand.")
        print(
            f"{players_hand} = {sum(players_hand)} < {dealers_hand} = {sum(dealers_hand)}"
        )
        print("You lost\n")
        play_again = input(
            "Do want to play again?\nType 'y' for Yes or 'n' for No.\n"
        ).lower()
        if play_again == "y":
            os.system("cls" if os.name == "nt" else "clear")
            main()
        else:
            sys.exit(0)


def pick_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card


def add_cards_to_hands():
    cards_on_table = {"players_hand": [], "dealers_hand": []}
    for i in range(2):
        cards_on_table["players_hand"].append(card(True))
        cards_on_table["dealers_hand"].append(card(False))
    return cards_on_table


def card(for_player: bool):
    if for_player:
        card_drawn = pick_a_card()
        if not card_drawn == 11:
            return card_drawn
        else:
            print("You Drew an ACE.")
            one_or_eleven = int(
                input("Type 1 to count it as one or\nType 11 to count it as eleven\n")
            )
            if one_or_eleven == 1:
                return 1
            else:
                return 11
    else:
        return pick_a_card()


if __name__ == "__main__":
    main()
