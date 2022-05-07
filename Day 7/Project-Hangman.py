import random
import hang_art
import hang_words
word_list = hang_words.word_list

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# ran = random.randint(0, len(word_list)-1)
# chosen_word = word_list[ran]
# print(chosen_word)

# CLEAR Solution
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hang_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while not end_of_game:
    guess = input("Guess a letter: ").lower()

# Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(hang_art.stages[lives])