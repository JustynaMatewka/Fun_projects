MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def share_report(current_resources):
    """Print formated resources report"""
    print(f"Water: {current_resources['water']}ml\n"
          f"Milk: {current_resources['milk']}ml\n"
          f"Coffee: {current_resources['coffee']}g\n"
          f"Money: ${current_resources['money']}")


def check_resources(current_resources, coffee_type):
    """Take machine resources and user coffee type and check if there are enough ingredients return True/False"""
    for ingredient in MENU[coffee_type]['ingredients']:
        if not MENU[coffee_type]['ingredients'][ingredient] <= current_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.”")
            return False
    return True


def collect_coins():
    """Ask user to insert coins by its type and returns their calculated value"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction_successful(current_resources, given_coins, coffee_type):
    """Return True (and change to user if needed) when the payment is accepted,
    or False if money is insufficient"""
    if given_coins < MENU[coffee_type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if given_coins > MENU[coffee_type]['cost']:
        change = round(given_coins - MENU[coffee_type]['cost'], 2)
        print(f"Here is ${change} dollars in change.")

    current_resources['money'] += MENU[coffee_type]['cost']
    return True


def make_coffee(current_resources, coffee_type):
    """Main part in this file
    take machine resources and coffee type chosen by user and process coffee or return None if error occurs"""
    if check_resources(current_resources, coffee_type):
        if check_transaction_successful(current_resources, collect_coins(), coffee_type):
            for ingredient in MENU[coffee_type]['ingredients']:
                current_resources[ingredient] -= MENU[coffee_type]['ingredients'][ingredient]
            print(f"Here is your {coffee_type}. Enjoy!")
        else:
            return
        return
    else:
        return



turn_on = True
#   Beginner values of machine resources
resources = {
    "water": 10000,
    "milk": 5000,
    "coffee": 760,
    "money": 0
}

while turn_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice == "report":
        share_report(resources)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        make_coffee(resources, user_choice)
    elif user_choice == "off":
        turn_on = False
        print("Coffee machine is going to sleep.")
    else:
        print(f"{user_choice.capitalize()} is a wrong input.")
