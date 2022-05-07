from unittest import skip
import caesarart

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(u_text, u_shift, u_direction):
    # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
    crypted = ""
    if u_direction == "decode":
        u_shift *= -1
    # TODO-3: What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

    for letter in u_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + u_shift
            crypted += alphabet[new_position]
        else:
            crypted += letter
    print(f"The {u_direction}d text is {crypted}")


# TODO-1: Import and print the logo from art.py when the program starts.
print(caesarart.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
shift = shift % 25

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
