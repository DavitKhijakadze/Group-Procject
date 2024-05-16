import random


def card_chooser(players):
    cards = [
        "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
        "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
        "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"
    ]

    random.shuffle(cards)

    all_player = []
    for _ in range(players):
        hand = []
        for _ in range(5):
            card = cards.pop()
            hand.append(card)
        all_player.append(hand)

    return all_player


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
            cards.remove(item)

    shuffle = random.choice(cards)

    return shuffle


# -----------------------------------------------------------------------------------------------

def points_counter(player_cards):
    points = 0

    for item in player_cards:
        if len(item) == 3:
            points += 10
        elif item[0].isdigit():
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
    colours = {"S": 0, "H": 0, "D": 0, "C": 0}

    for card in player_cards:
        suit = card[-1]
        colours[suit] += 1

    max_key = max(colours, key=lambda x: colours[x])

    return colours[max_key]


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


# -----------------------------------------------------------------------------------------------

def find_min_max(player_points: dict) -> tuple:
    max_points_counter = 0
    max_points_name = str()
    min_points_name = str()
    max_points = max(player_points.values())
    min_points = min(player_points.values())

    for player in player_points:
        if player_points[player] == max_points:
            max_points_name = player
            max_points_counter += 1
        if player_points[player] < max_points:
            min_points_name = player
            print(f"Player {min_points_name} lost the game.")

    return max_points_counter, max_points_name, max_points, min_points_name, min_points


# -----------------------------------------------------------------------------------------------

def won_by(method) -> str:
    if method == points_counter:
        return "Points"
    elif method == colours_counter:
        return "Colours"
    elif method == value_counter:
        return "Cards"

# -----------------------------------------------------------------------------------------------

def find_max_by_method(dealt_cards: dict, method) -> bool:
    player_points = dict()
    player_won_by = won_by(method)

    for name, cards in dealt_cards.items():
        player_points[name] = method(cards)

    max_points_counter, max_points_name, max_points, min_points_name, min_points = find_min_max(player_points)

    if max_points_counter == 1:
        cards = dealt_cards[max_points_name]
        print(f"Player {max_points_name} won by {player_won_by} with hand {cards}.")
        return True
    elif min_points_name != str() and min_points != max_points:
        dealt_cards.pop(min_points_name)


# -----------------------------------------------------------------------------------------------

def decide_winner(dealt_cards: dict):
    if find_max_by_method(dealt_cards, points_counter) or find_max_by_method(dealt_cards, colours_counter) or find_max_by_method(dealt_cards, value_counter):
        return
    else:
        print("Match ended with draw.")