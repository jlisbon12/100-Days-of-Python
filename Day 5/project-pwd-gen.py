# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pswd = ""
# for i in range(0, nr_letters):
#     ranlet = random.randint(0, len(letters)-1)
#     pswd += letters[ranlet]

# for x in range(0, nr_symbols):
#     ransym = random.randint(0, len(symbols)-1)
#     pswd += symbols[ransym]

# for x in range(0, nr_numbers):
#     rannum = random.randint(0, len(numbers)-1)
#     pswd += numbers[rannum]

# print(pswd)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pswd = ""
for i in range(0, nr_letters):
    ranlet = random.randint(0, len(letters)-1)
    pswd += letters[ranlet]

for x in range(0, nr_symbols):
    ransym = random.randint(0, len(symbols)-1)
    pswd += symbols[ransym]

for n in range(0, nr_numbers):
    rannum = random.randint(0, len(numbers)-1)
    pswd += numbers[rannum]

newpswd = ""
for r in pswd:
    ran = random.randint(0, len(pswd)-1)
    newpswd += pswd[ran]

print(newpswd)
