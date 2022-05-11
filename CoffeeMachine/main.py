from data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

money = {
    "quarter": 0,
    "dime": 0,
    "nickel": 0,
    "penny": 0,
}

# coffee types: "espresso", "latte", "cappuccino"

# Get input from user asking which type of coffee they would like: Espresso/latte/cappuccino
# When coffee type is chosen, check if resources are available to make drink
# if there are enough resources, check to see if money given is sufficient
# if not enough money, simple print statement saying money refunded, else process the transaction
# if too much money given, give back change an display amount (ROUND TO TWO DECIMAL PLACES)
# if transaction successful, reduce amount of resources available in coffee machine
# if all goes well, print enjoy your coffee as final step
# "off" to exit
# "report" to list the current available resources Water, milk, coffee, and money in the machine
# Coffee item structure:
# "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#
#


def display_resources():
    """Prints the key: value pairs in the resources dictionary"""
    for k, v in resources.items():
        if k == "money":
            print(f"{k}: ${v}")
            continue
        if k == "coffee":
            print(f"{k}: {v}g")
            continue
        print(f"{k}: {v}mL")


def display_menu():
    print("Here's the menu:")
    for i in MENU:
        print(f"'{i.capitalize()}' Price: ${MENU[i]['cost']}0")


def are_resources_available(coffee_type):
    """Checks to see if the coffee machine has enough Water, Milk, and Coffee to produce the given coffee type. Returns bool"""
    resource_expenditure = MENU[coffee_type]["ingredients"]
    issue_resource = None
    for i in resource_expenditure:
        if resource_expenditure[i] <= resources[i]:
            enough_resources = True
        else:
            enough_resources = False
            issue_resource = resource_expenditure[i]
            break
    return enough_resources, issue_resource


def get_coin_total_dollar_amount(dict):
    """Takes money dict and converts into single float point value rounded to two decimal places"""
    quarters = dict["quarter"] * 0.25
    dimes = dict["dime"] * 0.10
    nickels = dict["nickel"] * 0.05
    pennies = dict["penny"] * 0.01
    return round((quarters + dimes + nickels + pennies), 2)


def calculate_change(dollar_amount, coffee_type):
    cost = MENU[coffee_type]["cost"]
    return dollar_amount - cost


def enough_funds(coffee_type, dollar_amount):
    """Checks to see if given amount of money is enough to purchase specified coffee type. Returns bool"""
    cost = MENU[coffee_type]["cost"]
    if dollar_amount < cost:
        return False
    else:
        return True


def make_coffee(coffee_choice, money):
    success_message = f"Here is your {coffee_choice}!"
    if are_resources_available(coffee_choice) == True:
        if enough_funds(coffee_choice, money) == True:
            print(success_message)
        else:
            print("Insufficient Funds.")
    else:
        print("Insufficient resources.")


if __name__ == "__main__":
    print("Coffee Machine turned on! Welcome.")
    display_menu()
    coffee_choice = input(
        "What type of coffee would you like? (Espresso, Latte, or Cappuccino)"
    ).lower()
    money["quarter"] = int(input("How many quarters to insert?: "))
    money["dime"] = int(input("How many dimes to insert?: "))
    money["nickel"] = int(input("How many nickels to insert?: "))
    money["penny"] = int(input("How many pennies to insert?: "))
    # print(get_coin_total_dollar_amount(money))
    # print(are_resources_available("cappuccino"))
    # display_menu()
    # print(enough_funds("latte", 3.50))
    # print(f"${calculate_change(3.71, 'latte')}")
