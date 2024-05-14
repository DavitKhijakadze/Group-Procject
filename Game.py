from Func import *

PLAYER_NAMES = []
dealt_cards = {}

for player in range(3):
    name = input("Please enter your name: ")
    PLAYER_NAMES.append(name)

for player in PLAYER_NAMES:
    dealt_cards[player] = card_choicer()


for name, cards in dealt_cards.items():

    while True:
        hand = ', '.join(cards)
        user_answer = input(f"{name}, you are holding {hand}. \nif you want to change the card, choose the appropriate index from 1 to 5 inclusive, or enter 'NO': ")
        if user_answer == "NO":
            break
        elif user_answer in "12345":
            index = int(user_answer) - 1
            dealt_cards[name][index] = card_replacer(dealt_cards)
            break
        else:
            print("Please enter a correct answer!")

print()

for name, cards in dealt_cards.items():
    hand = ', '.join(cards)
    print(f"{name}, you are holding {hand}. Your total score is {points_counter(cards)}, The most common color is {colours_counter(cards)}, You have {value_counter(cards)} of a kind")

