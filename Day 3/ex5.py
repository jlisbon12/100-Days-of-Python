# 🚨 Don't change the code below 👇


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
score1 = 0
score2 = 0

name1.lower()
name2.lower()

score1 += int(name1.count("t"))
score1 += int(name1.count("r"))
score1 += int(name1.count("u"))
score1 += int(name1.count("e"))

score1 += int(name2.count("t"))
score1 += int(name2.count("r"))
score1 += int(name2.count("u"))
score1 += int(name2.count("e"))

score2 += int(name2.count("l"))
score2 += int(name2.count("o"))
score2 += int(name2.count("v"))
score2 += int(name2.count("e"))

score2 += int(name1.count("l"))
score2 += int(name1.count("o"))
score2 += int(name1.count("v"))
score2 += int(name1.count("e"))

total_score = str(score1) + str(score2)


if(int(total_score) < 10 or int(total_score) > 90):
    print(
        f"Your score is {total_score}, you go together like coke and mentos.")
elif(40 < int(total_score) < 50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
