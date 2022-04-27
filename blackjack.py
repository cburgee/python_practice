import random

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
correct_suite = ["J", "Q", "K"]
player_hand = []
dealer_hand = []
WIN = 1
LOSS = -1
DRAW = 0
point_totals = []


def draw_card(deck):
    return random.choice(deck)


def draw(hand):
    hand.append(draw_card(card_deck))
    if sum(hand) > 21:
        for i in range(0, len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                break
    return hand


def show_card():
    p_hand = correct_format(player_hand)
    d_hand = correct_format(dealer_hand)
    print(f"Your cards are: {p_hand}\nDealer's cards: {d_hand}")


def correct_format(list):
    new_list = []
    for i in list:
        if isinstance(i, str) == False:
            if i == 10:
                new_list.append(random.choice(correct_suite))
            elif i == 11 or i == 1:
                new_list.append("A")
            else:
                new_list.append(i)
    return new_list


def get_hand_total(hand):
    return sum(hand)


def calculate_winner(point_totals):
    p_points = point_totals[0]
    d_points = point_totals[1]
    if p_points == d_points:
        return DRAW

    if p_points > 21:
        if d_points > 21:
            return DRAW
        else:
            return LOSS
    elif p_points > d_points or d_points > 21:
        return WIN
    else:
        return LOSS


print("Welcome to BlackJack!")
for i in range(0, 2):
    player_hand = draw(player_hand)
    dealer_hand = draw(dealer_hand)
formatted_player_hand = correct_format(player_hand)
formatted_dealer_hand = correct_format(dealer_hand)
show_card()
do_add_card = input("Type 'y' to get another card, type 'n' to pass.").lower()
while get_hand_total(player_hand) <= 21 and do_add_card == "y":
    draw(player_hand)
    show_card()
    do_add_card = input("Type 'y' to get another card, type 'n' to pass.").lower()
if get_hand_total(dealer_hand) < 17:
    draw(dealer_hand)
show_card()
point_totals.append(get_hand_total(player_hand))
point_totals.append(get_hand_total(dealer_hand))
print(point_totals)
winner = calculate_winner(point_totals)
if winner == WIN:
    print("You Win!")
if winner == DRAW:
    print("It's a Draw!")
if winner == LOSS:
    print("You lose!")
