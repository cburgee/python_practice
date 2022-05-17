from data import MENU

available_resources = {
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

is_on = True


def display_available_resources():
    """Prints the key: value pairs in the resources dictionary"""
    for k, v in available_resources.items():
        if k == "money":
            v = float(v)
            print(f"{k.capitalize()}: ${round(v, 2)}")
            continue
        if k == "coffee":
            print(f"{k.capitalize()}: {v}g")
            continue
        print(f"{k.capitalize()}: {v}mL")


def display_menu():
    print("Here's the menu:")
    for i in MENU:
        print(f"'{i.capitalize()}' Price: ${MENU[i]['cost']}0")


def are_resources_available(coffee_type):
    """Checks to see if the coffee machine has enough Water, Milk, and Coffee to produce the given coffee type. Returns bool"""
    resource_expenditure = MENU[coffee_type]["ingredients"]
    issue_resource = None
    for i in resource_expenditure:
        if resource_expenditure[i] <= available_resources[i]:
            enough_resources = True
        else:
            enough_resources = False
            issue_resource = i
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
    return round(dollar_amount - cost, 2)


def enough_funds(coffee_type, dollar_amount):
    """Checks to see if given amount of money is enough to purchase specified coffee type. Returns bool"""
    cost = MENU[coffee_type]["cost"]
    if dollar_amount < cost:
        return False
    else:
        return True


def update_machine_values(coffee_type):
    spent_resources = MENU[coffee_type]["ingredients"]
    available_resources["money"] += MENU[coffee_type]["cost"]
    for i in spent_resources:
        available_resources[i] -= spent_resources[i]


def make_coffee(coffee_choice, dollar_amount):
    success_message = f"Here is your {coffee_choice}! Enjoy!"
    resource_availability = are_resources_available(coffee_choice)
    if resource_availability[0] == True:
        if enough_funds(coffee_choice, dollar_amount) == True:
            update_machine_values(coffee_choice)
            print(success_message)
            print(
                f"Here is your change!: ${calculate_change(dollar_amount, coffee_choice)}"
            )
        else:
            print("Insufficient Funds.")
            print(f"Here is your full refund: ${dollar_amount}")
    else:
        print(f"Insufficient resources. Not enough {resource_availability[1]}")
        print(f"Here is your full refund: ${dollar_amount}")


if __name__ == "__main__":
    print("Coffee Machine turned on! Welcome.")
    display_menu()
    while is_on:
        coffee_choice = input(
            "What type of coffee would you like? (Espresso, Latte, or Cappuccino)"
        ).lower()
        if coffee_choice == "report":
            display_available_resources()
            continue
        if coffee_choice == "off":
            break
        print("Please insert coins.")
        money["quarter"] = int(input("How many quarters: "))
        money["dime"] = int(input("How many dimes: "))
        money["nickel"] = int(input("How many nickels: "))
        money["penny"] = int(input("How many pennies: "))
        inserted_money = get_coin_total_dollar_amount(money)
        make_coffee(coffee_choice, inserted_money)
