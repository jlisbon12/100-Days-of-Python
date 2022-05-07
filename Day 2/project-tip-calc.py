# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the Tip Calculator!")
bill = int(input("What was the total bill?\n $"))
p = int(input("How many people will split?\n "))
per = int(input("What percent would you like to tip? [10%, 12%, 15%] "))

amt = (bill * (1+(per/100)))/5


print("Each person will pay: ${:0.2f}".format(amt))
