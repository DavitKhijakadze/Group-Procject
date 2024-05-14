import random

def card_choicer():

    cards = [
    "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
    "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
    "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
    "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"
    ]

    shuffle = random.choices(cards, k=5)

    return shuffle

# -----------------------------------------------------------------------------------------------

def card_replacer(players_cards):

    cards = [
    "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
    "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
    "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
    "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"
    ]
        
    for value in players_cards.values():
        for item in value:
            if item in cards:
                cards.remove(item)

    shuffle = random.choice(cards)

    return shuffle

# -----------------------------------------------------------------------------------------------

def points_counter(player_cards):

    points = 0

    for item in player_cards:
        if len(item) == 3:
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

# -----------------------------------------------------------------------------------------------

def colours_counter(player_cards):

    colors = {"S": 0, "H": 0, "D": 0, "C": 0}
    
    for card in player_cards:
        suit = card[-1]
        colors[suit] += 1

    max_key = max(colors, key=lambda x: colors[x])

    return max_key

# -----------------------------------------------------------------------------------------------

def value_counter(player_cards):

    values = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
              "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0, "K": 0, "A": 0}
    
    for item in player_cards:
        if len(item) == 3:
            key = item[:2]
            values[key] += 1
        else:
            key = item[0]
            values[key] += 1

    max_key = max(values, key=lambda x: values[x])

    return values[max_key]

