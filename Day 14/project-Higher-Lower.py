from operator import is_
from webbrowser import get
from hlart import logo, vs
from game_data import data
import random
import os


def clearConsole():
    command = 'clear'
    os.system(command)


# Generate a random account from the game data.
def get_random_account():
    return random.choice(data)


# Format account data into printable format.
def format_data(account):
    name = account['name']
    desc = account['description']
    country = account['country']

    return f"{name}, a {desc} from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    # Score Keeping.
    score = 0
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    # Make game repeatable.
    while game_continue:
        account_a = account_b
        account_b = get_random_account()
        # Make B become the next A.
        while account_a == account_b:
            account_b = get_random_account()

        # Ask user for a guess.
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # Get follower count.
        a_foll_count = account_a['follower_count']
        b_foll_count = account_b['follower_count']

        # Check if user is correct.
        is_correct = check_answer(guess, a_foll_count, b_foll_count)

        # Clear screen between rounds.
        clearConsole()

        print(logo)
        # Feedback.
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
