# calculator
from calcart import logo
# add


def add(n1, n2):
    return n1 + n2

# substract


def subtract(n1, n2):
    return n1 - n2

# multiply


def multiply(n1, n2):
    return n1 * n2

# divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """Calculate numbers"""
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    end_calc = False
    while not end_calc:
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("What's the next number?: "))
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(
            f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ").lower()
        if should_continue == "n":
            end_calc = True
            calculator()
        else:
            num1 = answer


calculator()
