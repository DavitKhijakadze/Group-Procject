from Func import *

NUMBER_OF_PLAYERS = 3

dealt_cards = {}

deal_cards = card_chooser(NUMBER_OF_PLAYERS)

player_index = 0

while len(dealt_cards) != NUMBER_OF_PLAYERS:
    name = input("Please enter your name: ")
    if not (name in dealt_cards):
        dealt_cards[name] = deal_cards[player_index]
        player_index += 1
    else:
        print(f"Player by name {name} already exists.")

print()

for name, cards in dealt_cards.items():

    while True:
        hand = ', '.join(cards)
        user_answer = input(f"{name}, you are holding {hand}. \nif you want to change the card, choose the appropriate index from 1 to 5 inclusive, or enter 'NO': ")
        print()
        if user_answer == "NO":
            break
        elif user_answer in "12345":
            index = int(user_answer) - 1
            dealt_cards[name][index] = card_replacer(dealt_cards)
            break
        else:
            print("Please enter a correct answer!")

for name, cards in dealt_cards.items():
    hand = ', '.join(cards)
    print(f"{name}, you are holding {hand}. Your total score is {points_counter(cards)}, The maximum number of colors is {colours_counter(cards)}, You have {value_counter(cards)} of a kind")

print()

decide_winner(dealt_cards)
