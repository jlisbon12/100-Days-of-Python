import random

choice = input("Heads or Tails?\n").capitalize()

num = random.randint(0, 1)


if (num == 1):
    final = "Heads"
else:
    final = "Tails"

print(f"The coin flipped: {final}")


# Other option for input
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
