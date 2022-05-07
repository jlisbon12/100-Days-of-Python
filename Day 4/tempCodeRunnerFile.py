print("Computer chose:")
num = random.randint(0, 2)

if num == 0:
    print(rock)
elif num == 1:
    print(paper)
elif num == 2:
    print(scissors)

if(choice == 1 and num == 2 or choice == 0 and num == 1 or choice == 2 and num == 0):
    print("You lose")
elif(choice == num):
    print("It's a tie")
else:
    print("You win")
