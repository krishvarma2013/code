import random
import sys

cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

def calculate_hand_total(hand_of_cards):
    total_score = 0
    number_of_aces = 0

    for card in hand_of_cards:
        if card == "Ace":
            total_score += 11
            number_of_aces += 1
        elif card in ["King", "Queen", "Jack"]:
            total_score += 10
        else:
            total_score += int(card)

    while total_score > 21 and number_of_aces > 0:
        total_score -= 10
        number_of_aces -= 1

    return total_score

def give_a_card(hand_to_add_to):
    picked_card = random.choice(cards)
    hand_to_add_to.append(picked_card)
    return picked_card

def show_hands(player_cards, dealer_cards, hide_dealer_card_initially=True):
    print("\n--- What Everyone Has ---")
    print(f"Your Cards: {', '.join(player_cards)} (Your Score: {calculate_hand_total(player_cards)})")
    if hide_dealer_card_initially:
        print(f"Dealer's Cards: {dealer_cards[0]}, [Hidden Card]")
    else:
        print(f"Dealer's Cards: {', '.join(dealer_cards)} (Dealer's Score: {calculate_hand_total(dealer_cards)})")
    print("-------------------------\n")

def players_turn(player_cards, dealer_cards):
    while True:
        your_score = calculate_hand_total(player_cards)
        show_hands(player_cards, dealer_cards, hide_dealer_card_initially=True)

        if your_score == 21:
            print("Wow! You have exactly 21! Good job!")
            return False
        elif your_score > 21:
            print("Oh no! Your score is over 21! You BUSTED!")
            return True

        your_choice = input("Do you want to draw or stand? ").lower()
        if your_choice == "draw":
            new_card_you_got = give_a_card(player_cards)
            print(f"You drew a {new_card_you_got}.")
        elif your_choice == "stand":
            print("Okay, you decided to stand. Now it's the dealer's turn.")
            return False
        else:
            print("That's not a valid choice. Please type draw or stand.")

def dealers_turn(player_cards, dealer_cards):
    print("\n--- Dealer's Turn Now ---")
    print("The dealer shows their hidden card!")
    show_hands(player_cards, dealer_cards, hide_dealer_card_initially=False)

    while calculate_hand_total(dealer_cards) < 17:
        print("Dealer's score is less than 17, so the dealer takes another card.")
        new_card_dealer_got = give_a_card(dealer_cards)
        print(f"Dealer drew a {new_card_dealer_got}.")
        show_hands(player_cards, dealer_cards, hide_dealer_card_initially=False)

    dealers_final_score = calculate_hand_total(dealer_cards)
    if dealers_final_score > 21:
        print("The dealer's score is over 21! The dealer busted!")
        return True
    else:
        print(f"The dealer stands with a score of {dealers_final_score}.")
        return False

def figure_out_the_winner(player_cards, dealer_cards, amount_you_bet, your_money_now):
    your_final_score = calculate_hand_total(player_cards)
    dealers_final_score = calculate_hand_total(dealer_cards)

    print("\n--- Game Over! Who Won? ---")
    show_hands(player_cards, dealer_cards, hide_dealer_card_initially=False)

    you_busted = your_final_score > 21
    dealer_busted = dealers_final_score > 21

    if you_busted:
        print("You went over 21, so you lose this round. The dealer wins!")
        your_money_now -= amount_you_bet
    elif dealer_busted:
        print("The dealer went over 21, so the dealer loses! You WIN!")
        your_money_now += amount_you_bet
    elif your_final_score > dealers_final_score:
        print("Your score is higher than the dealer's! You WIN!")
        your_money_now += amount_you_bet
    elif dealers_final_score > your_final_score:
        print("The dealer's score is higher than yours. You lose this round.")
        your_money_now -= amount_you_bet
    else:
        print("It's a TIE! (They call this a 'push'). You get your money back.")

    print(f"You now have: {your_money_now}$")
    return your_money_now

def play_one_round(current_money_you_have):
    print(f"\n--- Starting a New Round! ---")
    print(f"You currently have: {current_money_you_have}$")

    if current_money_you_have <= 0:
        print("Oh no! You don't have any money left to bet. Game over!")
        return 0

    while True:
        try:
            bet_amount = int(input("How much money do you want to bet this round? "))
            if bet_amount <= 0:
                print("You need to bet a positive amount of money.")
            elif bet_amount > current_money_you_have:
                print(f"Whoa! You only have {current_money_you_have}$. We'll bet all of it for you.")
                bet_amount = current_money_you_have
            break
        except ValueError:
            print("That's not a number. Please type a number for your bet.")

    print(f"You bet {bet_amount}$. Good luck!")

    players_hand = []
    dealers_hand = []

    print("\nDealing out the first cards...")
    give_a_card(players_hand)
    give_a_card(dealers_hand)
    give_a_card(players_hand)
    give_a_card(dealers_hand)

    players_first_score = calculate_hand_total(players_hand)
    dealers_first_score = calculate_hand_total(dealers_hand)

    if players_first_score == 21 and len(players_hand) == 2:
        print("BLACKJACK! You got 21 with your first two cards!")
        if dealers_first_score == 21 and len(dealers_hand) == 2:
            print("The dealer also has Blackjack! It's a TIE (a push).")
            return current_money_you_have
        else:
            print("You win with Blackjack! You get extra money!")
            return current_money_you_have + int(bet_amount * 1.5)

    did_player_bust = players_turn(players_hand, dealers_hand)

    if did_player_bust:
        return figure_out_the_winner(players_hand, dealers_hand, bet_amount, current_money_you_have)

    did_dealer_bust = dealers_turn(players_hand, dealers_hand)

    return figure_out_the_winner(players_hand, dealers_hand, bet_amount, current_money_you_have)

def main_game_loop():
    your_total_money = random.randint(1000, 50000)
    print(f"Welcome to the Simple Blackjack Game! You start with: {your_total_money}$")

    while True:
        your_total_money = play_one_round(your_total_money)
        
        if your_total_money <= 0:
            print("You've run out of money! Thanks for playing!")
            break

        play_again_choice = input("Do you want to play another round? (type 'yes' or 'no'): ").lower()
        if play_again_choice != "yes":
            print(f"Thanks for playing! You are leaving with {your_total_money}$.")
            break

if __name__ == "__main__":
    main_game_loop()







































































  

'''import random
monkey = ["drippycheese", "friesbag", "moldycheese"]
monkey = random.choice(monkey)
player_input = input("what do you want to use: drippycheese (rock), friesbag (scissors), or moldycheese (paper) " )

if monkey == "drippycheese" and player_input == "friesbag":
  print ("monkey won")
if monkey == "friesbag" and player_input == "moldycheese":
  print ("monkey won")
if monkey == "moldycheese" and player_input == "drippycheese":
  print ("monkey won")
if player_input == "drippycheese" and monkey == "friesbag":
  print ("you won")
if player_input == "friesbag" and monkey == "moldycheese":
  print ("you won")
if player_input == "moldycheese" and monkey == "drippycheese":
  print ("you won")
if monkey == player_input:
  print ("tie")'''




