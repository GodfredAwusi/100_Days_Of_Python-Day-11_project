import random
import os
from art import logo

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    for card in cards:
        if card == 11 and sum(cards) > 21:
            card = 1
    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose!, computer has blackjack"
    elif player_score == 0:
        return "You have blackjack, you win!"
    elif player_score > 21:
        return "You went over, you lose!"
    elif computer_score > 21:
        return "Computer went over, you win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_cards = []
    computer_cards = []
    game_over = False
    print(logo)
    player_cards.extend([deal_card(), deal_card()])
    computer_cards.extend([deal_card(), deal_card()])

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        computer_first_card = computer_cards[0]

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_first_card}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            get_another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if get_another_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True
    while computer_score <= 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score=player_score, computer_score=computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    cls()
    play_game()  
