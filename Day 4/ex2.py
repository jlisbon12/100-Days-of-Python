import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

num = random.randint(0, len(names)-1)
draw = names[num]
print(f"{draw} is going to buy dinner today!")
