import art

def add(n1, n2):
    return n1 + n2

# my_favourite_operation = add
#
# print(my_favourite_operation(2, 3))

# TODO: Write out the other 3 functions - subtract, multiply, and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    continue_cal = True
    num1 = float(input("What's your first number?\n"))

    while continue_cal:
        for symbol in operations:
            print(symbol)
        choices = input("Choose the type of a mathematical operator:")
        num2 = float(input("What's your second number?\n"))
        answer  = (operations[choices](n1= num1, n2= num2))
        print(f"{num1} {choices} {num2} = {answer}")

        choice = input(f"If you want to continue calculating with {answer}, please type 'y' or type 'n' to start new calculation.\n")

        if choice == "y":
            num1 = answer
        else:
            continue_cal = False
            print("\n" * 40)
            calculator()

calculator()