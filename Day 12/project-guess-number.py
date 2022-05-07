# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

logo = """
                                                                
     ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
    a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
    8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
    "8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
     `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'      
     aa,    ,88                                             
     "Y8bbdP"                                              
"""


def easy_level():
    total_guess = 10
    match = False
    while not match:
        print(
            f"You have {total_guess} attempts remaining to guess the answer.")
        guess = int(input("Make a guess: "))

        if guess < answer:
            total_guess -= 1
            if total_guess == 0:
                print("Too low")
                print("You've run out of guesses, you lose.")
                match = True
            else:
                print("Too low.\nGuess again.")
        elif guess > answer:
            total_guess -= 1
            if total_guess == 0:
                print("Too low")
                print("You've run out of guesses, you lose.")
                match = True
            else:
                print("Too high.\nGuess again")
        else:
            print("You got it! The answer was 100.")
            match = True


def hard_level():
    total_guess = 5
    match = False
    while not match:
        print(
            f"You have {total_guess} attempts remaining to guess the answer.")
        guess = int(input("Make a guess: "))
        if guess < answer:
            total_guess -= 1
            if total_guess == 0:
                print("Too low")
                print("You've run out of guesses, you lose.")
                match = True
            else:
                print("Too low.\nGuess again.")
        elif guess > answer:
            total_guess -= 1
            if total_guess == 0:
                print("Too low")
                print("You've run out of guesses, you lose.")
                match = True
            else:
                print("Too high.\nGuess again")
        else:
            print("You got it! The answer was 100.")
            match = True


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


answer = random.randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

if level == "easy":
    easy_level()

if level == "hard":
    hard_level()
