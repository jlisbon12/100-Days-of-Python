# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
l = 0
n = 0

if(year % 400 == 0):
    l += 1
else:
    n += 1

if(n > l):
    print("Not a leap year")
else:
    print("Leap year!")
