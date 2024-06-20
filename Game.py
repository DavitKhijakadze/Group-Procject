from Func import *

number_of_players = int(input("Enter the number of players: "))
names_of_players = []
dealt_cards = {}

if len(dealt_cards) == 0:       
    while len(names_of_players) != number_of_players:
        name = input("Please enter your name: ")
        if name not in names_of_players:
            names_of_players.append(name)
        else:
            print(f"Player by name {name} already exists.")

while True:
    
    all_card_in_game = card_chooser(number_of_players)
    
    card_index = 0
    for player in names_of_players:
        dealt_cards[player] = all_card_in_game[card_index]
        card_index += 1

    print()

    for name, cards in dealt_cards.items():

        while True:
            hand = ', '.join(cards)
            user_answer = input(f"{name}, you are holding {hand}. \nif you want to change the card, choose the appropriate index from 1 to 5 inclusive, or enter 'NO': ")
            print()
            if user_answer == "NO":
                break
            elif user_answer in ["1", "2", "3", "4", "5"]:
                index = int(user_answer) - 1
                dealt_cards[name][index] = card_replacer(dealt_cards)
                break
            else:
                print("Please enter a correct answer!")

    for name, cards in dealt_cards.items():
        hand = ', '.join(cards)
        print(f"{name}, you are holding {hand}. Your total score is {points_counter(cards)}, The maximum number of colors is {colours_counter(cards)}, You have {value_counter(cards)} of a kind")

    print()

    loser = reveal_loser(dealt_cards)

    if loser == "Draw":
        print("it is draw, keep playing")
        exit()
    elif loser in dealt_cards.keys():
        print(f"{loser} left the game")
        print()
        print("-" * 100)
        del dealt_cards[loser]
        names_of_players.remove(loser)
    
    if len(dealt_cards.keys()) == 1:
        print(f"Congratulations {names_of_players[0]}, you won!")
        break