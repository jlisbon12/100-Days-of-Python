# Dictionary
#   {key:value}

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# Retriving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again"

# create empty dict
empty_dictionary = {}

# delete existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item
programming_dictionary["Bug"] = "A math in your program."
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
