"""
try : something that might cause an exception
except : do this if there was an exception
else : do this if there were no exceptions
finally : do this no matter what happens
"""

#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dict = {"key": "value"}
# value = a_dict["non-key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Orange"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as err_message:
#     print(f"The key {err_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise


# Raising exceptions
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)


# EXERCISE 1

# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)


# EXERCISE 2

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass



print(total_likes)




