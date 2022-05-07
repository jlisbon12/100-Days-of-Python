
# function with an input
def greet(name):
    print(f"Hello {name}")
    print(f"Bonjour {name}")
    print(f"Hola {name}")


name = "Jedae"
greet(name)

# Function with more than one input


def greet_with(name, location):
    print(f"Hello, {name}. You're from {location}")


greet_with("Jedae", "Atlanta")


# Functions with keyword arguments
def greet_key(name="Jedae", location="Atlanta"):
    print(f"Hey {name}, How's {location}?")


greet_key()
