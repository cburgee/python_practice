from art import logo, vs
from higher_lower_game_data import data as GAME_DATA
import random

HIGHER = 1
LOWER = 0
LOGO = logo
VS_ART = vs
score = 0
do_continue = True
element_a = None
element_b = None

# Create intro message for game
# pull element from game_data and save it to variable via function call
# save description to variable and print
# save follower count to variable
# EXAMPLE DATA SAMPLE:
# {
#         "name": "Instagram",
#         "follower_count": 346,
#         "description": "Social media platform",
#         "country": "United States",
# },
# ensure pulled elements are not the same
# get user input to decide which has a higher follower count
# if correct, take comparison object (B) and make it the A object then get a new B
# track score, one point if correct


def get_game_element():
    return GAME_DATA[random.randint(0, len(GAME_DATA) - 1)]


def display_choice(dict):
    name = dict["name"]
    description = dict["description"]
    country = dict["country"]
    if country == "United States":
        print(f"{name}, a {description}, from the {country}")
    else:
        print(f"{name}, a {description}, from {country}")


def less_than(dict_a, dict_b):
    followers_a = dict_a["follower_count"]
    followers_b = dict_b["follower_count"]
    if followers_a < followers_b:
        return LOWER
    else:
        return HIGHER


def display(elements):
    display_choice(elements[0])
    print(VS_ART + "\n")
    display_choice(elements[1])


def reset():
    global element_a
    global element_b
    element_a = element_b
    element_b = None


print(LOGO + "\n")
while do_continue:
    if not element_a:
        element_a = get_game_element()
    if not element_b:
        element_b = get_game_element()
    if element_a == element_b:
        element_a = get_game_element()
    comparison_result = less_than(element_a, element_b)
    display([element_a, element_b])
    guess = input("Who has more followers? 'A' or 'B' ").lower()

    won = (guess == "a" and comparison_result == 0) or (
        guess == "b" and comparison_result == 1
    )
    if won:
        score += 1
        reset()
        print(LOGO + "\n")
        print(f"You're Right! Your score: {score}")
    else:
        do_continue = False
        print(LOGO + "\n")
        print(f"Sorry, that's wrong. Final score: {score}")
