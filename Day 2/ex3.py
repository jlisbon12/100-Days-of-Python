# 🚨 Don't change the code below 👇
from imghdr import what


age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
whats_left = 90 - int(age)
days = whats_left * 365
weeks = whats_left * 52
month = whats_left * 12


print(f"You have {days} days, {weeks} weeks, and {month} months left.")
