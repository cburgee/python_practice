import random
from word_list import word_list
from hangman_art import stages, logo

word_selected = random.choice(word_list)
letter_set = set(word_selected)
under_score = list()
player_choices = set()
lives = 6

under_score = list()
game_finished = False
print(logo)


def player_choice():
    choice_letter = input("What letter would you like to choose? \n").lower()
    return choice_letter


for l in range(0, len(word_selected)):
    under_score.append("_")

while not game_finished:
    print(stages[lives])
    print(" ".join(under_score) + "\n")
    if len(letter_set) == 0:
        print("You win!")
        game_finished = True
    elif lives == 0:
        print("You lose!")
        game_finished = True
    else:
        choice = player_choice()
        if choice in player_choices:
            print("You have already played this letter!")
            continue
        player_choices.add(choice)
        if choice in letter_set:
            print("Letter found!")
            letter_set.remove(choice)
            for i in range(0, len(word_selected)):
                if word_selected[i] == choice:
                    under_score[i] = choice
        else:
            lives -= 1
            print("Letter not found!")
