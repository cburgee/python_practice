# Get first number input
# Get for operation to apply
# Get second number input
# ask if user wants to continue with previous output
# or start over with two new inputs

repeat = True
first_number = 1
second_number = 1
result = 0


def add(first_num, second_num):
    return first_num + second_num


def subtract(first_num, second_num):
    return first_num - second_num


def multiply(first_num, second_num):
    return first_num * second_num


def divide(first_num, second_num):
    return first_num / second_num


while repeat == True:
    first_number = float(input("What is the first number?: "))
    operation = input("'add', 'subtract', 'multiply', or 'divide'\n")
    second_number = float(input("What is your second number?: "))
    if operation == "add".lower():
        result = round(add(first_number, second_number), 2)
        print(f"{first_number} + {second_number} = {result}")
    elif operation == "subtract".lower():
        result = round(subtract(first_number, second_number), 2)
        print(f"{first_number} - {second_number} = {result}")
    elif operation == "multiply".lower():
        result = round(multiply(first_number, second_number), 2)
        print(f"{first_number} * {second_number} = {result}")
    else:
        result = round(divide(first_number, second_number), 2)
        print(f"{first_number} / {second_number} = {result}")
    do_continue = input("Type 'n' to start a new calculation, or 'x' to exit.\n")
    if do_continue == "x".lower():
        repeat = False
