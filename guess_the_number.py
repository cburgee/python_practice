import random

CORRECT = 0
TOO_LOW = 1
TOO_HIGH = 2
# Guess the number
# Welcome statement
# choose either easy or hard difficulty
# 5 attempts for hard, 10 for easy
# choose a number between 1 or 100
# get player guess, return too high, too low, or you got it correct


def get_random_number():
    return random.randint(2, 99)


def set_difficulty(choice):
    if choice == "easy":
        return 10
    if choice == "hard":
        return 5


def check_guess(number):
    global random_number
    if number == random_number:
        return CORRECT
    if number < random_number:
        return TOO_LOW
    if number > random_number:
        return TOO_HIGH


print(
    "Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100"
)
get_difficulty = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
guesses_left = set_difficulty(get_difficulty)
random_number = get_random_number()
print(f"You have {guesses_left} attempt(s) to guess the number.")
while guesses_left != 0:
    player_guess = int(input("Make a guess: "))
    did_win = check_guess(player_guess)
    if did_win == CORRECT:
        print(f"You guessed the number right! The number was: {random_number}")
        break
    if did_win == TOO_LOW:
        guesses_left -= 1
        print("Too low.\nGuess again.")
        print(f"You have {guesses_left} attempt(s) to guess the number.")
    if did_win == TOO_HIGH:
        print("Too high.\nGuess again.")
        print(f"Guesses left: {guesses_left}")
        guesses_left -= 1
print("You ran out of guesses! You lose.")
