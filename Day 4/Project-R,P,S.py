import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

image = [rock, paper, scissors]

print(image[choice])


print("Computer chose:")
num = random.randint(0, 2)

print(image[num])

if(choice == 1 and num == 2 or choice == 0 and num == 1 or choice == 2 and num == 0):
    print("You lose")
elif(choice == num):
    print("It's a tie")
else:
    print("You win")
