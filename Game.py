import random

# player_name_1 = input("Enter first player name: ")
# player_name_2 = input("Enter second player name: ")
# player_name_3 = input("Enter third player name: ")

player_1_cards = []
player_2_cards = []
player_3_cards = []

cards = [
    "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
    "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
    "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
    "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"
]

def card_choicer(player_name):
    
    while len(player_name) != 5:
        random_choice = random.choice(cards)
        player_name.append(random_choice)
        cards.remove(random_choice)

def points_counter(player_cards):
    points = 0
    for item in player_cards:
        if len(player_cards) == 3:
            points += 10
        if item[0].isdigit():
            points += int(item[0])
        if item[0] == "J":
            points += 11
        if item[0] == "Q":
            points += 12
        if item[0] == "K":
            points += 13
        if item[0] == "A":
            points += 20
    
    return points

def colours_counter(player_cards):
    colors = {"S": 0, "H": 0, "D": 0, "C": 0}
    
    for card in player_cards:
        suit = card[-1]
        colors[suit] += 1

    return colors

card_choicer(player_1_cards)
card_choicer(player_2_cards)
card_choicer(player_3_cards)

print(player_1_cards, f"point is - {points_counter(player_1_cards)}", colours_counter(player_1_cards))
print(player_2_cards, f"point is - {points_counter(player_2_cards)}", colours_counter(player_2_cards))
print(player_3_cards, f"point is - {points_counter(player_3_cards)}", colours_counter(player_3_cards))

